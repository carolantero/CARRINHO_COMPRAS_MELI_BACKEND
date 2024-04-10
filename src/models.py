from pydantic import BaseModel

class ShoppingCartItem(BaseModel):
    product_id: str
    product_title: str
    product_image: str
    product_price: float