from fastapi import APIRouter
from src.repository import RepositoryShoppingCart

router = APIRouter()

@router.get("/get_all_products", tags=["Produtos"])
def controller_get_all_products():
    try:
        repository: RepositoryShoppingCart = RepositoryShoppingCart()
        result: list = repository.get_all_products()

        return result
    except Exception as e:
        raise e