import reflex as rx
from app.states.state import HomePageState
from app.components.header import header
from app.components.footer import footer


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "A forma inteligente de usar cada ",
                rx.el.span(
                    "euro.",
                    class_name="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-purple-500 to-cyan-400",
                ),
                class_name="text-4xl md:text-6xl font-extrabold text-gray-900 tracking-tighter font-['Poppins'] text-center",
            ),
            rx.el.p(
                "Promoções verificadas, apps financeiras e dicas práticas para poupar em Portugal e Espanha.",
                class_name="mt-6 text-lg text-gray-600 max-w-2xl mx-auto text-center",
            ),
            rx.el.div(
                rx.el.a(
                    "Ver Promoções",
                    rx.icon("arrow-right", class_name="ml-2 h-5 w-5"),
                    href="/promotions",
                    class_name="flex items-center justify-center px-8 py-3 text-base font-medium text-white bg-blue-600 rounded-full hover:bg-blue-700 transition-transform duration-300 ease-in-out hover:scale-105 shadow-lg",
                ),
                rx.el.a(
                    "Entrar no Canal",
                    rx.icon("send", class_name="mr-2 h-5 w-5"),
                    href="#",
                    class_name="flex items-center justify-center px-8 py-3 text-base font-medium text-blue-600 bg-white rounded-full border border-gray-200 hover:bg-gray-100 transition-transform duration-300 ease-in-out hover:scale-105 shadow-lg",
                ),
                class_name="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4",
            ),
            class_name="py-20 md:py-32",
        )
    )


def promotion_card(promo: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=promo["image"],
                class_name="absolute inset-0 w-full h-full object-cover rounded-2xl",
            ),
            rx.el.div(class_name="absolute inset-0 bg-black/20 rounded-2xl"),
            rx.el.div(
                rx.el.h3(
                    promo["title"],
                    class_name="text-xl font-bold text-white font-['Poppins']",
                ),
                rx.el.p(promo["description"], class_name="mt-1 text-sm text-white/80"),
                class_name="absolute bottom-0 left-0 p-6",
            ),
        ),
        href=promo["link"],
        class_name="relative h-80 rounded-2xl overflow-hidden group transform hover:-translate-y-2 transition-transform duration-300 shadow-lg hover:shadow-2xl",
    )


def promotions_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Promoções em Destaque",
                class_name="text-3xl font-bold text-gray-900 text-center font-['Poppins']",
            ),
            rx.el.p(
                "Europa mais barata começa aqui. Poupa com inteligência.",
                class_name="mt-4 text-lg text-gray-600 text-center max-w-xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(HomePageState.featured_promotions, promotion_card),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
        ),
        class_name="py-16 bg-gray-50",
    )


def app_card(app: dict) -> rx.Component:
    return rx.el.div(
        rx.image(src=app["logo"], alt=f"Logo {app['name']}", class_name="h-12 w-12"),
        rx.el.h3(
            app["name"],
            class_name="mt-4 text-lg font-semibold text-gray-900 font-['Poppins']",
        ),
        rx.el.p(app["description"], class_name="mt-1 text-sm text-gray-600"),
        class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:border-blue-300 transition-all duration-300",
    )


def apps_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Apps que Fazem Poupar",
                class_name="text-3xl font-bold text-gray-900 text-center font-['Poppins']",
            ),
            rx.el.p(
                "Melhores apps e ferramentas para manter o teu dinheiro onde deve estar — contigo.",
                class_name="mt-4 text-lg text-gray-600 text-center max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(HomePageState.saving_apps, app_card),
                class_name="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
        ),
        class_name="py-16",
    )


def guide_card(guide: dict) -> rx.Component:
    return rx.el.a(
        rx.icon(guide["icon"], class_name="h-6 w-6 text-blue-600"),
        rx.el.span(guide["title"], class_name="text-base font-semibold text-gray-800"),
        href=guide["link"],
        class_name="flex items-center gap-4 p-4 bg-white rounded-xl border border-gray-200 hover:bg-gray-100 hover:shadow-md transition-all duration-300",
    )


def guide_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Guia de Poupança",
                class_name="text-3xl font-bold text-gray-900 text-center font-['Poppins']",
            ),
            rx.el.p(
                "Dicas e truques práticos para a tua vida financeira na Europa.",
                class_name="mt-4 text-lg text-gray-600 text-center",
            ),
            rx.el.div(
                rx.foreach(HomePageState.guides, guide_card),
                class_name="mt-12 grid grid-cols-2 md:grid-cols-4 gap-6",
            ),
        ),
        class_name="py-16 bg-gray-50",
    )


def community_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Junta-te à Comunidade",
                    class_name="text-3xl font-bold text-white font-['Poppins']",
                ),
                rx.el.p(
                    "Partilha dicas e encontra as melhores promoções em primeira mão.",
                    class_name="mt-2 text-lg text-white/80",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("send", class_name="h-5 w-5 mr-2"),
                        "Entrar no Telegram",
                        href="#",
                        class_name="flex items-center justify-center px-6 py-3 bg-white text-blue-600 font-medium rounded-full hover:bg-gray-200 transition-colors shadow-md",
                    ),
                    rx.el.a(
                        rx.icon("message-circle", class_name="h-5 w-5 mr-2"),
                        "Grupo WhatsApp",
                        href="#",
                        class_name="flex items-center justify-center px-6 py-3 bg-green-500 text-white font-medium rounded-full hover:bg-green-600 transition-colors shadow-md",
                    ),
                    class_name="mt-6 flex flex-col sm:flex-row gap-4",
                ),
            ),
            class_name="text-center",
        ),
        class_name="py-20 bg-gradient-to-r from-blue-600 via-purple-500 to-cyan-400",
    )


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero_section(),
        promotions_section(),
        apps_section(),
        guide_section(),
        community_section(),
        footer(),
        class_name="font-['Inter'] bg-white",
    )


from app.pages.promotions import promotions
from app.pages.ferramentas import ferramentas
from app.pages.guia import guia
from app.pages.comunidade import comunidade
from app.pages.sobre import sobre
from app.pages.afiliados import afiliados
from app.pages.admin_login import admin_login
from app.pages.admin_dashboard import admin_dashboard
from app.pages.not_found import not_found_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(promotions)
app.add_page(ferramentas)
app.add_page(guia)
app.add_page(comunidade)
app.add_page(sobre)
app.add_page(afiliados)
app.add_page(admin_login, route="/admin/login")
app.add_page(admin_dashboard, route="/admin/dashboard")
app.add_page(not_found_page, route="/404")