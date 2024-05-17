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

    Retorna:
        Uma lista de dicionários com todos os produtos.

    Lança:
        HTTPException: Se ocorrer algum erro ao tentar obter os produtos.
    """
    try:
        result: list = repository.get_all_products()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao tentar obter todos os produtos.") from e
    
@router.get("/get_products_by_category", tags=["Produtos por Categoria"])
def controller_get_products_by_category(category: str):
    """
    Obtém os produtos disponíveis de acordo com sua categoria.

    Args:
        category: uma categoria do tipo 'str' que será usada como parametro na url da api externa.
        
    Retorna:
        Uma lista de dicionários com todos os produtos.

    Lança:
        HTTPException: Se a categoria não for válida ou não retornar resultados.
    """
    try:
        result: list = repository.get_products_by_category(category=category)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    
@router.post("/post_cart_products/", tags=["Adicionar Itens ao Carrinho"])
def controller_post_cart_products(items: List[ShoppingCartItem]):
    """
    Adiciona itens ao carrinho de compras.

    Args:
        items: Uma lista de objetos ShoppingCartItem representando os itens a serem adicionados ao carrinho.

    Retorna:
        Uma lista de dicionários representando os itens adicionados ao carrinho.

    Lança:
        HTTPException: Se ocorrer algum erro ao tentar adicionar os itens ao carrinho.
    """
    try:
        result: list = repository.post_cart_products(items=items)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao tentar adicionar itens ao carrinho.") from e
    
@router.get("/get_cart_products/", tags=["Obter Itens do Carrinho"])
def controller_get_cart_products():
    """
    Obtém os itens adicionados no carrinho de compras.

    Retorna:
        Uma lista de dicionários representando os itens dentro do carrinho de compras.

    Lança:
        HTTPException: Se ocorrer algum erro ao tentar obter os itens do carrinho.
    """
    try:
        result: list = repository.get_cart_products()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao tentar obter os itens do carrinho.") from e
    
@router.delete("/delete_cart_product/{item_id}", tags=["Deletar Item do Carrinho"])
def controller_delete_cart_product(product_id: str):
    """
    Deleta um item do carrinho de compras com base no ID.

    Args:
        product_id: O ID do item a ser deletado.

    Retorna:
        Uma mensagem de sucesso ou erro.

    Lança:
        HTTPException: Se ocorrer algum erro ao tentar deletar o item do carrinho.
    """
    try:
        result = repository.delete_cart_product(product_id=product_id)

        if not result:
            raise HTTPException(status_code=404, detail="Item não encontrado no carrinho.")
        return {"detail": "Item deletado com sucesso do carrinho."}
    
    except Exception as e:
       raise HTTPException(status_code=500, detail="Erro interno do servidor ao tentar deletar o item do carrinho.") from e