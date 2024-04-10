from fastapi import APIRouter, HTTPException
from src.models import ShoppingCartItem
from src.repository import RepositoryShoppingCart
from typing import List


router = APIRouter()

shopping_cart = []

@router.get("/get_all_products", tags=["Produtos"])
def controller_get_all_products():
    try:
        repository: RepositoryShoppingCart = RepositoryShoppingCart()
        result: list = repository.get_all_products()

        return result
    except Exception as e:
        raise e
    
@router.post("/post_cart_products/", tags=["Adicionar Itens ao Carrinho"])
def add_to_cart(items: List[ShoppingCartItem]):
    try:
        global shopping_cart
        shopping_cart = []
        shopping_cart.extend(items)
        return shopping_cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_cart_products/", tags=["Obter Itens do Carrinho"])
def get_cart():
    try:
        global shopping_cart
        return shopping_cart
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))