import reflex as rx


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors",
    )


def header() -> rx.Component:
    return rx.el.header(
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
                rx.el.nav(
                    nav_link("Promoções", "/promotions"),
                    nav_link("Ferramentas", "/ferramentas"),
                    nav_link("Afiliados", "/afiliados"),
                    nav_link("Guias", "/guia"),
                    nav_link("Comunidade", "/comunidade"),
                    class_name="hidden md:flex items-center gap-6",
                ),
            ),
            rx.el.div(
                rx.el.a(
                    "Login Admin",
                    href="/admin/login",
                    class_name="hidden sm:inline-block text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors mr-4",
                ),
                rx.el.a(
                    "Ver Promoções",
                    href="/promotions",
                    class_name="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors shadow-sm",
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between w-full",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200 px-4 sm:px-6 lg:px-8 h-16 flex items-center",
    )