import reflex as rx
from typing import TypedDict


class Promotion(TypedDict):
    id: int
    image: str
    title: str
    description: str
    link: str


class AppTool(TypedDict):
    id: int
    logo: str
    name: str
    description: str


class Guide(TypedDict):
    id: int
    icon: str
    title: str
    link: str


class HomePageState(rx.State):
    """Manages the state for the EuroSmart homepage."""

    featured_promotions: list[Promotion] = [
        {
            "id": 1,
            "image": "/promos/tech.png",
            "title": "50€ de Desconto em Gadgets",
            "description": "Tecnologia de ponta mais acessível.",
            "link": "#",
        },
        {
            "id": 2,
            "image": "/promos/travel.png",
            "title": "Viagens de Fim-de-Semana",
            "description": "Até 30% de desconto em estadias.",
            "link": "#",
        },
        {
            "id": 3,
            "image": "/promos/food.png",
            "title": "Supermercado Inteligente",
            "description": "Poupe 15% nas suas compras.",
            "link": "#",
        },
        {
            "id": 4,
            "image": "/promos/fashion.png",
            "title": "Moda Sustentável",
            "description": "20% off em marcas selecionadas.",
            "link": "#",
        },
    ]
    saving_apps: list[AppTool] = [
        {
            "id": 1,
            "logo": "/logos/revolut.svg",
            "name": "Revolut",
            "description": "Contas multi-moeda e cartões virtuais.",
        },
        {
            "id": 2,
            "logo": "/logos/wise.svg",
            "name": "Wise",
            "description": "Transferências internacionais baratas.",
        },
        {
            "id": 3,
            "logo": "/logos/toogoodtogo.svg",
            "name": "Too Good To Go",
            "description": "Salve comida e poupe dinheiro.",
        },
        {
            "id": 4,
            "logo": "/logos/booking.svg",
            "name": "Booking",
            "description": "Ofertas em hotéis e voos.",
        },
    ]
    guides: list[Guide] = [
        {"id": 1, "icon": "euro", "title": "Abrir Conta na UE", "link": "#"},
        {"id": 2, "icon": "plane", "title": "Viajar Barato", "link": "#"},
        {"id": 3, "icon": "shopping-cart", "title": "Compras Online", "link": "#"},
        {"id": 4, "icon": "home", "title": "Poupar em Casa", "link": "#"},
    ]