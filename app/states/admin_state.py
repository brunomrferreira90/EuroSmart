import reflex as rx
import os
from app.states.promotions_state import PromotionsState, DetailedPromotion
from typing import Literal


class AdminState(rx.State):
    """Manages the state for the admin panel."""

    email: str = ""
    password: str = ""
    is_authenticated: bool = False
    error_message: str = ""
    show_add_modal: bool = False
    show_delete_confirm: bool = False
    promotion_to_delete_id: int | None = None

    @rx.event
    def login(self, form_data: dict) -> rx.event.EventSpec:
        """Logs the admin in."""
        self.email = form_data.get("email", "")
        self.password = form_data.get("password", "")
        admin_email = "admin@eurosmart.com"
        admin_password = "password123"
        if self.email == admin_email and self.password == admin_password:
            self.is_authenticated = True
            self.error_message = ""
            return rx.redirect("/admin/dashboard")
        else:
            self.error_message = "Credenciais inválidas. Tente novamente."
            self.password = ""
            return rx.toast.error("Login falhou!")

    @rx.event
    def logout(self) -> rx.event.EventSpec:
        """Logs the admin out."""
        self.is_authenticated = False
        self.email = ""
        self.password = ""
        return rx.redirect("/admin/login")

    @rx.event
    def check_auth(self):
        """Checks if the user is authenticated and redirects if not."""
        if not self.is_authenticated:
            return rx.redirect("/admin/login")

    @rx.event
    def toggle_add_modal(self):
        self.show_add_modal = not self.show_add_modal

    @rx.event
    async def add_promotion(self, form_data: dict):
        promo_state = await self.get_state(PromotionsState)
        current_promos = promo_state.all_promotions
        new_id = max([p["id"] for p in current_promos] + [0]) + 1
        new_promo: DetailedPromotion = {
            "id": new_id,
            "image": form_data.get("image", "/placeholder.svg"),
            "title": form_data.get("title", ""),
            "description": form_data.get("description", ""),
            "link": form_data.get("link", "#"),
            "country": form_data.get("country", "BOTH"),
            "category": form_data.get("category", "Apps"),
            "badge": form_data.get("badge", ""),
            "old_price": float(form_data["old_price"])
            if form_data.get("old_price")
            else None,
            "new_price": float(form_data["new_price"])
            if form_data.get("new_price")
            else None,
        }
        promo_state.all_promotions.append(new_promo)
        self.show_add_modal = False
        return rx.toast.success("Promoção adicionada com sucesso!")

    @rx.event
    def confirm_delete_promotion(self, promo_id: int):
        self.promotion_to_delete_id = promo_id
        self.show_delete_confirm = True

    @rx.event
    def cancel_delete(self):
        self.promotion_to_delete_id = None
        self.show_delete_confirm = False

    @rx.event
    async def delete_promotion(self):
        if self.promotion_to_delete_id is not None:
            promo_state = await self.get_state(PromotionsState)
            promo_state.all_promotions = [
                p
                for p in promo_state.all_promotions
                if p["id"] != self.promotion_to_delete_id
            ]
            self.cancel_delete()
            return rx.toast.error("Promoção removida.")

    @rx.var
    async def filtered_promotions(self) -> list[DetailedPromotion]:
        """Gets the filtered promotions from the promotions state."""
        promo_state = await self.get_state(PromotionsState)
        return promo_state.filtered_promotions