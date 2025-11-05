import reflex as rx
from app.components.header import header
from app.components.footer import footer


def guide_item(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-blue-600"),
            class_name="flex items-center justify-center h-16 w-16 bg-blue-100 rounded-xl",
        ),
        rx.el.h3(
            title, class_name="mt-6 text-xl font-bold text-gray-900 font-['Poppins']"
        ),
        rx.el.p(description, class_name="mt-2 text-gray-600"),
        class_name="p-8 bg-white rounded-2xl border border-gray-200 shadow-sm",
    )


def guia() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Guia: Como Poupar na Europa",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tighter font-['Poppins'] text-center",
                ),
                rx.el.p(
                    "Dicas e truques práticos para a sua vida financeira na Europa, desde abrir conta a viajar barato.",
                    class_name="mt-6 text-lg text-gray-600 max-w-2xl mx-auto text-center",
                ),
                class_name="py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                guide_item(
                    "university",
                    "Abrir Conta Bancária na UE",
                    "Guia completo para não-residentes e estudantes. Comparamos os melhores bancos digitais como Revolut, Wise e N26 para evitar taxas escondidas.",
                ),
                guide_item(
                    "plane",
                    "Estratégias para Viajar Barato",
                    "Aprenda a usar agregadores de voos, programas de fidelidade e as melhores épocas para comprar bilhetes e poupar centenas de euros.",
                ),
                guide_item(
                    "shopping-cart",
                    "Compras Online Inteligentes",
                    "Descubra extensões de browser para cashback, sites de comparação de preços e como tirar partido de promoções sazonais.",
                ),
                guide_item(
                    "home",
                    "Reduzir Despesas em Casa",
                    "Dicas práticas para poupar em eletricidade, água e gás. Renegocie contratos e adote hábitos que fazem a diferença na fatura mensal.",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto",
            ),
            class_name="py-16 px-4",
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )