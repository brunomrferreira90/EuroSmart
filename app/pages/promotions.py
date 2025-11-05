import reflex as rx
from app.states.promotions_state import PromotionsState
from app.components.header import header
from app.components.footer import footer


def badge_component(text: rx.Var[str]) -> rx.Component:
    return rx.el.span(
        text,
        class_name=rx.cond(
            text == "Top Deal",
            "bg-yellow-100 text-yellow-800 text-xs font-medium px-2 py-1 rounded-full",
            rx.cond(
                text == "Termina Breve",
                "bg-red-100 text-red-800 text-xs font-medium px-2 py-1 rounded-full",
                rx.cond(
                    text == "Cashback",
                    "bg-green-100 text-green-800 text-xs font-medium px-2 py-1 rounded-full",
                    "bg-gray-100 text-gray-800 text-xs font-medium px-2 py-1 rounded-full",
                ),
            ),
        ),
    )


def promotion_card(promo: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=promo["image"],
                class_name="w-full h-48 object-cover rounded-t-2xl",
                alt=promo["title"],
            ),
            rx.cond(promo["badge"] != "", badge_component(promo["badge"]), rx.el.div()),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.h3(
                promo["title"],
                class_name="font-bold text-lg text-gray-900 font-['Poppins'] truncate",
            ),
            rx.el.p(
                promo["description"],
                class_name="text-sm text-gray-600 mt-1 h-10 overflow-hidden",
            ),
            rx.el.div(
                rx.cond(
                    promo["old_price"].is_not_none(),
                    rx.el.div(
                        rx.el.span(
                            f"{promo['new_price'].to_string()}€",
                            class_name="text-xl font-bold text-blue-600",
                        ),
                        rx.el.span(
                            f"{promo['old_price'].to_string()}€",
                            class_name="text-sm text-gray-500 line-through ml-2",
                        ),
                        class_name="flex items-baseline h-7",
                    ),
                    rx.el.div(class_name="h-7"),
                ),
                class_name="mt-4",
            ),
            rx.el.a(
                "Obter Oferta",
                rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                href=promo["link"],
                class_name="mt-4 w-full flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-transform duration-200 ease-in-out hover:scale-105 shadow-md",
            ),
            class_name="p-4 flex flex-col justify-between flex-1",
        ),
        class_name="bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col",
    )


def filters_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "Todas as Promoções",
                class_name="text-4xl font-bold text-gray-900 font-['Poppins']",
            ),
            rx.el.p(
                "Filtre e encontre as melhores oportunidades para poupar.",
                class_name="mt-2 text-lg text-gray-600",
            ),
            class_name="text-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400",
                ),
                rx.el.input(
                    placeholder="Pesquisar por título ou descrição...",
                    on_change=PromotionsState.set_search_term,
                    default_value=PromotionsState.search_term,
                    class_name="w-full pl-10 pr-4 py-2 border rounded-lg focus:ring-blue-500 focus:border-blue-500",
                ),
                class_name="relative w-full lg:w-1/3",
            ),
            rx.el.div(
                rx.el.button(
                    "Todos",
                    on_click=lambda: PromotionsState.set_country_filter("ALL"),
                    class_name=rx.cond(
                        PromotionsState.country_filter == "ALL",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-blue-600 text-white",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-white text-gray-700",
                    ),
                ),
                rx.el.button(
                    "Portugal",
                    on_click=lambda: PromotionsState.set_country_filter("PT"),
                    class_name=rx.cond(
                        PromotionsState.country_filter == "PT",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-blue-600 text-white",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-white text-gray-700",
                    ),
                ),
                rx.el.button(
                    "Espanha",
                    on_click=lambda: PromotionsState.set_country_filter("ES"),
                    class_name=rx.cond(
                        PromotionsState.country_filter == "ES",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-blue-600 text-white",
                        "px-4 py-2 rounded-lg font-medium transition-colors bg-white text-gray-700",
                    ),
                ),
                class_name="flex items-center gap-2 p-1 bg-gray-100 rounded-lg",
            ),
            rx.el.select(
                rx.el.option("Todas as Categorias", value="ALL"),
                rx.foreach(
                    PromotionsState.categories,
                    lambda category: rx.el.option(category, value=category),
                ),
                on_change=PromotionsState.set_category_filter,
                default_value=PromotionsState.category_filter,
                class_name="border rounded-lg px-4 py-2 focus:ring-blue-500 focus:border-blue-500",
            ),
            class_name="mt-8 flex flex-col lg:flex-row items-center justify-between gap-4",
        ),
        class_name="py-16 bg-gray-50 px-4",
    )


def promotions_grid() -> rx.Component:
    return rx.el.section(
        rx.cond(
            PromotionsState.filtered_promotions.length() > 0,
            rx.el.div(
                rx.foreach(PromotionsState.filtered_promotions, promotion_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8",
            ),
            rx.el.div(
                rx.icon("search-x", class_name="h-16 w-16 text-gray-400"),
                rx.el.h3(
                    "Nenhuma promoção encontrada",
                    class_name="mt-4 text-xl font-semibold text-gray-700",
                ),
                rx.el.p(
                    "Tente ajustar os seus filtros ou termo de pesquisa.",
                    class_name="mt-2 text-gray-500",
                ),
                class_name="text-center py-20 flex flex-col items-center justify-center col-span-full",
            ),
        ),
        class_name="py-12 px-4",
    )


def promotions() -> rx.Component:
    return rx.el.main(
        header(),
        filters_section(),
        promotions_grid(),
        footer(),
        class_name="font-['Inter'] bg-white",
    )