from fastapi import APIRouter, HTTPException
from src.models import ShoppingCartItem
from src.repository import RepositoryShoppingCart
from typing import List


router = APIRouter()
repository = RepositoryShoppingCart()

@router.get("/get_all_products", tags=["Produtos"])
def controller_get_all_products():
    try:
        result: list = repository.get_all_products()

        return result
    except Exception as e:
        raise e
    
@router.post("/post_cart_products/", tags=["Adicionar Itens ao Carrinho"])
def controller_post_cart_products(items: List[ShoppingCartItem]):
    try:
        result: list = repository.post_cart_products(items)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_cart_products/", tags=["Obter Itens do Carrinho"])
def controller_get_cart_products():
    try:
        result: list = repository.get_cart_products()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))