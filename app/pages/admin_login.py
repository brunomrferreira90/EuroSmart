import reflex as rx
from app.states.admin_state import AdminState
from app.components.header import header
from app.components.footer import footer


def admin_login() -> rx.Component:
    """The admin login page."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("euro", class_name="h-8 w-8 text-white"),
                        class_name="p-3 bg-gradient-to-r from-blue-600 to-cyan-400 rounded-xl",
                    ),
                    href="/",
                ),
                rx.el.h2(
                    "Acesso Restrito",
                    class_name="mt-8 text-2xl font-bold text-gray-900 font-['Poppins']",
                ),
                rx.el.p(
                    "Use as suas credenciais para aceder ao painel de administração.",
                    class_name="mt-2 text-sm text-gray-600",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Email",
                                htmlFor="email",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.input(
                                type="email",
                                id="email",
                                name="email",
                                placeholder="admin@eurosmart.com",
                                class_name="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                            ),
                            class_name="space-y-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Password",
                                htmlFor="password",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.input(
                                type="password",
                                id="password",
                                name="password",
                                placeholder="••••••••",
                                class_name="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                            ),
                            class_name="space-y-1",
                        ),
                        rx.cond(
                            AdminState.error_message != "",
                            rx.el.div(
                                rx.icon(
                                    "flag_triangle_right",
                                    class_name="h-4 w-4 mr-2 text-red-500",
                                ),
                                rx.el.p(
                                    AdminState.error_message,
                                    class_name="text-sm text-red-600",
                                ),
                                class_name="flex items-center p-2 bg-red-50 rounded-md",
                            ),
                            None,
                        ),
                        rx.el.button(
                            "Login",
                            rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                            type="submit",
                            class_name="w-full flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors shadow-sm disabled:opacity-50",
                        ),
                        class_name="space-y-6",
                    ),
                    on_submit=AdminState.login,
                    class_name="mt-8",
                ),
                class_name="w-full max-w-md",
            ),
            class_name="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-gray-50",
        ),
        class_name="font-['Inter'] bg-white",
    )