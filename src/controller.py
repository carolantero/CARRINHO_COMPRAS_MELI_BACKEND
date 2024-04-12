from fastapi import APIRouter, HTTPException
from src.models import ShoppingCartItem
from src.repository import RepositoryShoppingCart
from typing import List


router = APIRouter()
repository = RepositoryShoppingCart()

@router.get("/get_all_products", tags=["Produtos"])
def controller_get_all_products():
    """
    Obtém todos os produtos disponíveis.

    Retorna: Uma lista de dicionários com todos os produtos.
    """
    try:
        result: list = repository.get_all_products()

        return result
    except Exception as e:
        raise e
    
@router.post("/post_cart_products/", tags=["Adicionar Itens ao Carrinho"])
def controller_post_cart_products(items: List[ShoppingCartItem]):
    """
    Adiciona itens ao carrinho de compras.

    Args: items: Uma lista de objetos ShoppingCartItem representando os itens a serem adicionados ao carrinho.
    Retorna: Uma lista de dicionários representando os itens adicionados ao carrinho.
    """
    try:
        result: list = repository.post_cart_products(items=items)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_cart_products/", tags=["Obter Itens do Carrinho"])
def controller_get_cart_products():
    """
    Obtém os itens adicionados no carrinho de compras.

    Retorna: Uma lista de dicionários representando os itens dentro do carrinho de compras.
    """
    try:
        result: list = repository.get_cart_products()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))