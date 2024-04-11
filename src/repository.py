import requests
from fastapi import HTTPException

class RepositoryShoppingCart:
    def __init__(self):
        """
        Inicializa um novo objeto RepositoryShoppingCart.
        """
        self.shopping_cart = []

    def _get_data_from_meliapi(self) -> list:
        """
        Obtém dados da API externa (acesse: 'https://developers.mercadolibre.com/' para saber mais), para produtos de uma determinada categoria.

        Retorna: Uma lista de dicionários representando os produtos obtidos.
        """
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
        """
        Organiza a lista de produtos recebida em um formato específico.

        Args: products_list: Uma lista de dicionários representando os produtos que devem ser formatados.
        Retorna: Uma lista de dicionários representando os produtos já formatados.
        """
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
        """
        Obtém todos os produtos disponíveis da API externa e os organiza.

        Retorna: Uma lista de dicionários representando os produtos organizados e formatados.
        """
        try:
            data_products: list = self._get_data_from_meliapi()

            result: list = self._organize_products_list(products_list=data_products) 

             
            return result
        except Exception as e:
                raise e
        
    def post_cart_products(self, items: list) -> list:
        """
        Adiciona itens ao carrinho de compras.

        Args: items: Uma lista de dicionários representando os itens a serem adicionados ao carrinho.
        Retorna: Uma lista de dicionários representando os itens adicionados ao carrinho.
        """
        try:
            self.shopping_cart.clear()
            self.shopping_cart.extend(items)

            result: list = self.shopping_cart

            return result
        
        except Exception as e:
                raise e


    def get_cart_products(self) -> list:
        """
        Obtém os itens do carrinho de compras.

        Retorna: Uma lista de dicionários representando os itens no carrinho de compras.
        """
        try:  
            result: list = self.shopping_cart

            return result
    
        except Exception as e:
                raise e
