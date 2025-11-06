import reflex as rx
import os
import subprocess
import logging
import asyncio
from github import Github
from github.GithubException import UnknownObjectException


class DeployState(rx.State):
    """Manages the state for the deployment process."""

    is_deploying: bool = False
    deploy_status: str = "idle"
    deploy_logs: list[str] = []
    github_token_present: bool = False
    repo_owner: str = "brunomrferreira90"
    repo_name: str = "brunomrferreira90.github.io"
    branch: str = "main"

    @rx.var
    def deployed_url(self) -> str:
        return f"https://{self.repo_owner}.github.io/"

    @rx.event
    def check_github_token(self):
        """Checks if the GitHub token is available."""
        self.github_token_present = "GITHUB_TOKEN" in os.environ
        if not self.github_token_present:
            self.deploy_logs.append(
                "✗ GITHUB_TOKEN não encontrado nas variáveis de ambiente."
            )

    @rx.event(background=True)
    async def auto_deploy(self):
        """Exports the app and deploys to GitHub Pages."""
        async with self:
            if not self.github_token_present:
                self.deploy_logs.append(
                    "Deploy cancelado. Token do GitHub não está configurado."
                )
                yield rx.toast.error("GITHUB_TOKEN não encontrado!")
                return
            self.is_deploying = True
            self.deploy_status = "exporting"
            self.deploy_logs = ["Iniciando deploy..."]
        process = await asyncio.create_subprocess_exec(
            "reflex",
            "export",
            "--frontend-only",
            "--no-zip",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        async with self:
            if process.returncode != 0:
                self.is_deploying = False
                self.deploy_status = "error"
                self.deploy_logs.append("Falha ao exportar a aplicação.")
                self.deploy_logs.append(stderr.decode())
                yield rx.toast.error("Erro no export do Reflex!")
                return
            self.deploy_logs.append("✓ Aplicação exportada com sucesso.")
            self.deploy_status = "uploading"
            self.deploy_logs.append("A fazer upload para o GitHub...")
        try:
            github_token = os.getenv("GITHUB_TOKEN")
            g = Github(github_token)
            repo = g.get_repo(f"{self.repo_owner}/{self.repo_name}")
            frontend_path = "frontend/dist"
            if not os.path.isdir(frontend_path):
                raise FileNotFoundError(
                    f"Diretório de export não encontrado: {frontend_path}"
                )
            for root, _, files in os.walk(frontend_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    repo_path = os.path.relpath(file_path, frontend_path).replace(
                        "\\", "/"
                    )
                    with open(file_path, "rb") as f:
                        content = f.read()
                    try:
                        existing_file = repo.get_contents(repo_path, ref=self.branch)
                        repo.update_file(
                            path=repo_path,
                            message=f"Deploy: update {repo_path}",
                            content=content,
                            sha=existing_file.sha,
                            branch=self.branch,
                        )
                        log_msg = f"✓ Ficheiro atualizado: {repo_path}"
                    except UnknownObjectException as e:
                        logging.exception(f"Error creating file: {e}")
                        repo.create_file(
                            path=repo_path,
                            message=f"Deploy: create {repo_path}",
                            content=content,
                            branch=self.branch,
                        )
                        log_msg = f"✓ Ficheiro criado: {repo_path}"
                    async with self:
                        self.deploy_logs.append(log_msg)
                    yield
            async with self:
                self.deploy_status = "success"
                self.deploy_logs.append("🎉 Deploy concluído com sucesso!")
                self.deploy_logs.append(f"Acesse o site em: {self.deployed_url}")
                self.is_deploying = False
                yield rx.toast.success("Deploy realizado!")
                return
        except Exception as e:
            logging.exception(f"Deployment failed: {e}")
            async with self:
                self.is_deploying = False
                self.deploy_status = "error"
                self.deploy_logs.append(f"Ocorreu um erro no deploy: {str(e)}")
                yield rx.toast.error("Falha no deploy para o GitHub!")
                return