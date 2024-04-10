import requests
from fastapi import HTTPException

class RepositoryShoppingCart:
    # def __init__() -> None:
    #     ...

    def _get_data_from_meliapi(self) -> list:
        try:
            category: str = 'eletrodomestico'
            url: str = f'https://api.mercadolibre.com/sites/MLB/search?q={category}'
            response: requests.models.Response = requests.get(url)
            data: dict = response.json()

            result: list = data['results']
             
            return result
        except Exception as e:
                raise e
        
    def _organize_products_list(self, products_list: list) -> list:
        try:
            result: list = []

            for item in products_list:
                format_dict: dict = {
                    "product_id": item["id"],
                    "product_title": item["title"],
                    "product_image": item["thumbnail"].replace("I.jpg", "W.jpg"),
                    "product_price": item["price"]
                }
                result.append(format_dict)
            
            return result
        except Exception as e:
                raise e
         

    def get_all_products(self) -> list:
        try:
            data_products: list = self._get_data_from_meliapi()

            result: list = self._organize_products_list(products_list=data_products) 

             
            return result
        except Exception as e:
                raise e
