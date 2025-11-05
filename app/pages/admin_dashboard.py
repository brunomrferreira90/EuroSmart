import reflex as rx
from app.states.admin_state import AdminState
from app.states.promotions_state import PromotionsState


def add_promotion_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                rx.icon("circle_plus", class_name="mr-2"),
                "Adicionar Promoção",
                class_name="flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-blue-700 transition-colors",
            ),
            on_click=AdminState.toggle_add_modal,
        ),
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title(
                "Adicionar Nova Promoção", class_name="text-lg font-bold"
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.input(
                        name="title",
                        placeholder="Título",
                        required=True,
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.input(
                        name="description",
                        placeholder="Descrição",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.input(
                        name="image",
                        placeholder="URL da Imagem",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.input(
                        name="link",
                        placeholder="Link de Afiliado",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.input(
                        name="old_price",
                        placeholder="Preço Antigo",
                        type="number",
                        step="0.01",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.input(
                        name="new_price",
                        placeholder="Preço Novo",
                        type="number",
                        step="0.01",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.select(
                        rx.foreach(
                            PromotionsState.categories,
                            lambda c: rx.el.option(c, value=c),
                        ),
                        name="category",
                        default_value="Tecnologia",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.select(
                        rx.el.option("Ambos", value="BOTH"),
                        rx.el.option("Portugal", value="PT"),
                        rx.el.option("Espanha", value="ES"),
                        name="country",
                        default_value="BOTH",
                        class_name="w-full p-2 border rounded",
                    ),
                    rx.el.select(
                        rx.el.option("Nenhum", value=""),
                        rx.el.option("Top Deal", value="Top Deal"),
                        rx.el.option("Termina Breve", value="Termina Breve"),
                        rx.el.option("Cashback", value="Cashback"),
                        name="badge",
                        default_value="",
                        class_name="w-full p-2 border rounded",
                    ),
                    class_name="grid grid-cols-2 gap-4 my-4",
                ),
                rx.el.div(
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            "Cancelar",
                            on_click=AdminState.toggle_add_modal,
                            class_name="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg font-medium",
                        )
                    ),
                    rx.el.button(
                        "Adicionar",
                        type="submit",
                        class_name="bg-blue-600 text-white px-4 py-2 rounded-lg font-medium",
                    ),
                    class_name="flex justify-end gap-4 mt-4",
                ),
                on_submit=AdminState.add_promotion,
            ),
        ),
        open=AdminState.show_add_modal,
    )


def delete_confirm_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title("Confirmar Remoção"),
            rx.radix.primitives.dialog.description(
                "Tem a certeza que quer remover esta promoção? Esta ação não pode ser desfeita."
            ),
            rx.el.div(
                rx.el.button(
                    "Cancelar",
                    on_click=AdminState.cancel_delete,
                    class_name="bg-gray-200 px-4 py-2 rounded-lg",
                ),
                rx.el.button(
                    "Remover",
                    on_click=AdminState.delete_promotion,
                    class_name="bg-red-500 text-white px-4 py-2 rounded-lg",
                ),
                class_name="flex justify-end gap-4 mt-4",
            ),
        ),
        open=AdminState.show_delete_confirm,
    )


def promotions_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th("ID", class_name="text-left p-2"),
                    rx.el.th("Título", class_name="text-left p-2"),
                    rx.el.th("País", class_name="text-left p-2"),
                    rx.el.th("Categoria", class_name="text-left p-2"),
                    rx.el.th("Ações", class_name="text-right p-2"),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    AdminState.filtered_promotions,
                    lambda promo: rx.el.tr(
                        rx.el.td(promo["id"], class_name="p-2"),
                        rx.el.td(promo["title"], class_name="p-2"),
                        rx.el.td(promo["country"], class_name="p-2"),
                        rx.el.td(promo["category"], class_name="p-2"),
                        rx.el.td(
                            rx.el.button(
                                rx.icon("trash-2", class_name="h-4 w-4"),
                                on_click=lambda: AdminState.confirm_delete_promotion(
                                    promo["id"]
                                ),
                                class_name="text-red-500 hover:text-red-700 p-1",
                            ),
                            class_name="text-right p-2",
                        ),
                        class_name="border-b hover:bg-gray-50",
                    ),
                )
            ),
            class_name="w-full table-auto",
        ),
        class_name="bg-white p-4 rounded-lg shadow-sm border mt-8",
    )


def admin_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Painel de Administração",
                class_name="text-3xl font-bold text-gray-900 font-['Poppins']",
            ),
            rx.el.button(
                "Logout",
                on_click=AdminState.logout,
                class_name="px-4 py-2 bg-gray-200 text-gray-800 rounded-lg font-medium hover:bg-gray-300",
            ),
            class_name="flex justify-between items-center p-6 border-b bg-white",
        ),
        rx.el.main(
            rx.el.div(
                rx.el.h2(
                    "Visão Geral", class_name="text-xl font-semibold text-gray-800"
                ),
                add_promotion_modal(),
                class_name="flex justify-between items-center mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Total de Promoções",
                        class_name="text-sm font-medium text-gray-500",
                    ),
                    rx.el.p(
                        PromotionsState.total_promotions.to_string(),
                        class_name="text-3xl font-bold text-gray-900",
                    ),
                    class_name="bg-white p-6 rounded-xl border shadow-sm",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
            ),
            promotions_table(),
            delete_confirm_dialog(),
            class_name="p-6",
        ),
        on_mount=AdminState.check_auth,
        class_name="bg-gray-50 min-h-screen",
    )