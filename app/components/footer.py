import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("euro", class_name="h-6 w-6 text-white"),
                        class_name="p-2 bg-gradient-to-r from-blue-600 to-cyan-400 rounded-lg",
                    ),
                    rx.el.span(
                        "EuroSmart",
                        class_name="text-lg font-bold text-gray-900 font-['Poppins']",
                    ),
                    href="/",
                    class_name="flex items-center gap-2",
                ),
                rx.el.p(
                    "A forma inteligente de usar cada euro.",
                    class_name="text-sm text-gray-600 mt-2",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Este site contém links de afiliados. Mantemos transparência e só recomendamos o que acreditamos trazer valor real.",
                    class_name="text-xs text-gray-500 text-center md:text-right max-w-sm",
                )
            ),
            class_name="flex flex-col md:flex-row items-center justify-between gap-6",
        ),
        rx.el.div(
            class_name="mt-8 border-t border-gray-200 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4"
        ),
        rx.el.div(
            rx.el.p(
                f"© {datetime.date.today().year} EuroSmart. Todos os direitos reservados.",
                class_name="text-sm text-gray-500",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "twitter",
                        class_name="h-5 w-5 text-gray-500 hover:text-blue-600",
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.icon(
                        "instagram",
                        class_name="h-5 w-5 text-gray-500 hover:text-blue-600",
                    ),
                    href="#",
                ),
                class_name="flex items-center gap-4",
            ),
        ),
        class_name="bg-gray-50 px-4 sm:px-6 lg:px-8 py-12",
    )