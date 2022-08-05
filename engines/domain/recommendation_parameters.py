from typing import TypedDict


class RecommendationParams(TypedDict):
    store_id: str
    subsidiary_id: str
    product: str
    shopping_cart_items: list
