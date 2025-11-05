import reflex as rx
from app.components.header import header
from app.components.footer import footer


def affiliate_step(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-blue-600"),
            class_name="flex items-center justify-center h-16 w-16 bg-blue-100 rounded-full",
        ),
        rx.el.h3(
            title,
            class_name="mt-5 text-xl font-semibold text-gray-800 font-['Poppins']",
        ),
        rx.el.p(description, class_name="mt-2 text-gray-600"),
        class_name="text-center",
    )


def afiliados() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Ganha Dinheiro com a EuroSmart",
                    class_name="text-4xl md:text-5xl font-extrabold text-white tracking-tighter font-['Poppins'] text-center",
                ),
                rx.el.p(
                    "Junta-te ao nosso programa de afiliados e ganha comissões partilhando as melhores promoções e ferramentas de poupança.",
                    class_name="mt-6 text-lg text-white/80 max-w-3xl mx-auto text-center",
                ),
                rx.el.a(
                    "Quero ser Afiliado",
                    rx.icon("rocket", class_name="ml-2"),
                    href="#",
                    class_name="mt-10 inline-flex items-center justify-center px-8 py-3 text-base font-medium text-blue-600 bg-white rounded-full hover:bg-gray-100 transition-transform duration-300 ease-in-out hover:scale-105 shadow-lg",
                ),
                class_name="py-20 md:py-28 flex flex-col items-center",
            ),
            class_name="bg-gradient-to-r from-blue-600 via-purple-500 to-cyan-400",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Como Funciona?",
                    class_name="text-3xl font-bold text-gray-900 text-center font-['Poppins']",
                ),
                rx.el.p(
                    "É simples, rápido e transparente. Comece a ganhar em 3 passos.",
                    class_name="mt-4 text-lg text-gray-600 text-center max-w-xl mx-auto",
                ),
                rx.el.div(
                    affiliate_step(
                        "user-plus",
                        "1. Regista-te",
                        "Preenche o nosso formulário de inscrição rápido. A aprovação é quase imediata.",
                    ),
                    affiliate_step(
                        "share-2",
                        "2. Partilha",
                        "Recebe os teus links de afiliado exclusivos para as nossas promoções e ferramentas.",
                    ),
                    affiliate_step(
                        "euro",
                        "3. Ganha",
                        "Ganha uma comissão por cada utilizador que se registe ou compre através dos teus links.",
                    ),
                    class_name="mt-16 grid grid-cols-1 md:grid-cols-3 gap-12 max-w-5xl mx-auto",
                ),
            ),
            class_name="py-20 px-4",
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )