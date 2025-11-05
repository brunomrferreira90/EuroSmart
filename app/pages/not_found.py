import reflex as rx
from app.components.header import header
from app.components.footer import footer


def not_found_page() -> rx.Component:
    """A página 404 personalizada que redireciona para a página inicial."""
    return rx.el.main(
        header(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Página Não Encontrada (404)",
                    class_name="text-4xl font-extrabold text-gray-900 tracking-tight font-['Poppins']",
                ),
                rx.el.p(
                    "A página que procura não existe. Será redirecionado para a página inicial.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                rx.el.a(
                    "Voltar à Página Inicial",
                    href="/",
                    class_name="mt-8 inline-flex items-center px-6 py-3 text-base font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors",
                ),
                class_name="text-center",
            ),
            class_name="flex items-center justify-center flex-1 py-20",
        ),
        footer(),
        class_name="font-['Inter'] bg-white flex flex-col min-h-screen",
    )