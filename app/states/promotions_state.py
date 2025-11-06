import reflex as rx
from typing import TypedDict, Literal


class DetailedPromotion(TypedDict):
    id: int
    image: str
    title: str
    description: str
    link: str
    country: Literal["PT", "ES", "BOTH"]
    category: str
    badge: Literal["Top Deal", "Termina Breve", "Cashback", ""]
    old_price: float | None
    new_price: float | None


class PromotionsState(rx.State):
    """Manages the state for the promotions page."""

    all_promotions: list[DetailedPromotion] = [
        {
            "id": 1,
            "image": "/promos/tech.png",
            "title": "50€ de Desconto em Gadgets",
            "description": "Tecnologia de ponta mais acessível com este cupão exclusivo.",
            "link": "#",
            "country": "PT",
            "category": "Tecnologia",
            "badge": "Top Deal",
            "old_price": 299.99,
            "new_price": 249.99,
        },
        {
            "id": 2,
            "image": "/promos/travel.png",
            "title": "Viagens de Fim-de-Semana",
            "description": "Até 30% de desconto em estadias selecionadas na Europa.",
            "link": "#",
            "country": "BOTH",
            "category": "Viagens",
            "badge": "Termina Breve",
            "old_price": None,
            "new_price": None,
        },
        {
            "id": 3,
            "image": "/promos/food.png",
            "title": "Supermercado Inteligente",
            "description": "Poupe 15% nas suas compras online em supermercados parceiros.",
            "link": "#",
            "country": "ES",
            "category": "Supermercado",
            "badge": "Cashback",
            "old_price": 100.0,
            "new_price": 85.0,
        },
        {
            "id": 4,
            "image": "/promos/fashion.png",
            "title": "Moda Sustentável com Desconto",
            "description": "20% off em marcas de moda sustentável selecionadas.",
            "link": "#",
            "country": "PT",
            "category": "Beleza",
            "badge": "",
            "old_price": 75.0,
            "new_price": 60.0,
        },
        {
            "id": 5,
            "image": "/placeholder.svg",
            "title": "App Financeiro Bónus",
            "description": "Abra conta e receba 10€ de bónus de boas-vindas.",
            "link": "#",
            "country": "ES",
            "category": "Finanças",
            "badge": "Top Deal",
            "old_price": None,
            "new_price": None,
        },
        {
            "id": 6,
            "image": "/placeholder.svg",
            "title": "Plano de Internet Fibra",
            "description": "Adesão com 50% de desconto nos primeiros 3 meses.",
            "link": "#",
            "country": "BOTH",
            "category": "Tecnologia",
            "badge": "",
            "old_price": 39.99,
            "new_price": 19.99,
        },
    ]
    search_term: str = ""
    country_filter: Literal["ALL", "PT", "ES"] = "ALL"
    category_filter: str = "ALL"
    categories: list[str] = [
        "Tecnologia",
        "Supermercado",
        "Viagens",
        "Apps",
        "Finanças",
        "Beleza",
    ]

    @rx.var
    def filtered_promotions(self) -> list[DetailedPromotion]:
        """Filters promotions based on search, country, and category."""
        return [
            promo
            for promo in self.all_promotions
            if (
                self.search_term.lower() in promo["title"].lower()
                or self.search_term.lower() in promo["description"].lower()
            )
            and (
                self.country_filter == "ALL"
                or promo["country"] == self.country_filter
                or promo["country"] == "BOTH"
            )
            and (
                self.category_filter == "ALL"
                or promo["category"] == self.category_filter
            )
        ]

    @rx.var
    def total_promotions(self) -> int:
        """Returns the total number of promotions."""
        return len(self.all_promotions)