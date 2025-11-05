import reflex as rx
from app.components.header import header
from app.components.footer import footer


def sobre() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Sobre o EuroSmart",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tighter font-['Poppins'] text-center",
                ),
                rx.el.p(
                    "A nossa missão é simplificar a poupança para quem vive na Europa.",
                    class_name="mt-6 text-lg text-gray-600 max-w-2xl mx-auto text-center",
                ),
                class_name="py-16 md:py-24 bg-gray-50",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "A nossa história",
                        class_name="text-3xl font-bold text-gray-900 font-['Poppins']",
                    ),
                    rx.el.p(
                        "O EuroSmart nasceu da nossa própria necessidade de navegar no complexo mundo financeiro da Europa. Cansados de taxas escondidas, promoções enganosas e falta de informação clara, decidimos criar a plataforma que gostaríamos de ter tido. A nossa equipa verifica cada promoção e testa cada ferramenta para garantir que apenas recomendamos o que realmente traz valor.",
                        class_name="mt-4 text-gray-600 space-y-4",
                    ),
                    rx.el.p(
                        "Acreditamos que poupar não deve ser complicado. Com as ferramentas e a informação certas, qualquer pessoa pode otimizar as suas finanças e viver melhor. Junte-se a nós nesta jornada rumo à inteligência financeira.",
                        class_name="mt-4 text-gray-600",
                    ),
                    class_name="max-w-2xl mx-auto",
                ),
                class_name="py-16 px-4",
            )
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )