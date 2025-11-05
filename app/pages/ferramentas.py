import reflex as rx
from app.components.header import header
from app.components.footer import footer
from app.states.state import HomePageState


def app_tool_card(app: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=app["logo"],
                alt=f"Logo {app['name']}",
                class_name="h-16 w-16 rounded-2xl object-contain",
            ),
            rx.el.div(
                rx.el.h3(
                    app["name"],
                    class_name="text-xl font-bold text-gray-900 font-['Poppins']",
                ),
                rx.el.p(app["description"], class_name="mt-2 text-gray-600"),
                class_name="flex-1",
            ),
            rx.el.div(rx.icon("arrow-up-right", class_name="h-5 w-5 text-gray-400")),
            class_name="flex items-start gap-6",
        ),
        href="#",
        class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:border-blue-300 transition-all duration-300 block",
    )


def ferramentas() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Ferramentas para Poupar",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tighter font-['Poppins'] text-center",
                ),
                rx.el.p(
                    "As melhores apps e ferramentas para manter o seu dinheiro onde deve estar: consigo.",
                    class_name="mt-6 text-lg text-gray-600 max-w-2xl mx-auto text-center",
                ),
                class_name="py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.foreach(HomePageState.saving_apps, app_tool_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto",
            ),
            class_name="py-16 px-4",
        ),
        footer(),
        class_name="font-['Inter'] bg-white",
    )