from fastapi import APIRouter

router = APIRouter()

@router.get("/get_all_products", tags=["Produtos"])
def controller_get_all_products():
    try:
        result = True

        return result
    except Exception as e:
        raise e