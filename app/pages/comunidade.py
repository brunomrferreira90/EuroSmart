import reflex as rx
from app.components.header import header
from app.components.footer import footer


def community_card(
    icon: str,
    title: str,
    description: str,
    button_text: str,
    href: str,
    color_class: str,
) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-12 w-12"),
        rx.el.h3(title, class_name="mt-4 text-2xl font-bold font-['Poppins']"),
        rx.el.p(description, class_name="mt-2 text-gray-200 max-w-sm mx-auto"),
        rx.el.a(
            button_text,
            href=href,
            class_name=f"mt-6 inline-block px-8 py-3 font-medium rounded-full transition-transform hover:scale-105 {color_class}",
        ),
        class_name="text-center text-white",
    )


def comunidade() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Junte-se à Comunidade EuroSmart",
                    class_name="text-4xl md:text-5xl font-extrabold text-white tracking-tighter font-['Poppins'] text-center",
                ),
                rx.el.p(
                    "Partilhe dicas e encontre as melhores promoções em primeira mão.",
                    class_name="mt-6 text-lg text-white/80 max-w-2xl mx-auto text-center",
                ),
                class_name="py-16 md:py-24",
            ),
            rx.el.div(
                community_card(
                    "send",
                    "Canal Telegram",
                    "Receba as melhores promoções e alertas de poupança diretamente no seu telemóvel. Sem spam, só valor.",
                    "Entrar no Telegram",
                    "#",
                    "bg-white text-blue-600",
                ),
                community_card(
                    "message-circle",
                    "Grupo WhatsApp",
                    "Converse com outros membros, partilhe as suas dicas e tire dúvidas sobre finanças e poupança.",
                    "Juntar-se ao Grupo",
                    "#",
                    "bg-green-500 text-white",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto",
            ),
            class_name="py-16 bg-gradient-to-r from-blue-600 via-purple-500 to-cyan-400 px-4",
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )