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
        Obtém dados de todos os produtos da API externa (acesse: 'https://developers.mercadolibre.com/' para saber mais).

        Retorna: Uma lista de dicionários representando os produtos obtidos.
        """
        try:
            url: str = f'https://api.mercadolibre.com/sites/MLB/search?q=all'
            response: requests.models.Response = requests.get(url)
            response.raise_for_status()

            data: dict = response.json()

            result: list = data['results']
             
            return result
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail="Erro ao se comunicar com a API externa.") from e
        

    def _get_data_from_meliapi_by_category(self, category: str) -> list:
        """
        Obtém dados da API externa (acesse: 'https://developers.mercadolibre.com/' para saber mais), para produtos de uma determinada categoria.

        Args:
            category: uma categoria do tipo 'str' que será usada como parametro na url da api externa.
            
        Retorna:
            Uma lista de dicionários representando os produtos obtidos.

        Lança:
            HTTPException: Se a categoria não for válida ou não retornar resultados.
        """
        try:
            url: str = f'https://api.mercadolibre.com/sites/MLB/search?q={category}'
            response: requests.models.Response = requests.get(url)
            response.raise_for_status()

            data: dict = response.json()

            result: list = data.get('results', [])

            if not result:
                raise HTTPException(status_code=404, detail="Categoria não é válida ou não retornou resultados. Por favor, tente outra categoria.")

            return result
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail="Erro ao se comunicar com a API externa.") from e
        

    def _organize_products_list(self, products_list: list) -> list:
        """
        Organiza a lista de produtos recebida em um formato específico.

        Args: products_list: Uma lista de dicionários representando os produtos que devem ser formatados.
        Retorna: Uma lista de dicionários representando os produtos já formatados.
        """
        try:
            result: list = []

            for item in products_list:
                truncated_title: str = self._truncated_text(max_text_length=60, text=item["title"])
                format_dict: dict = {
                    "product_id": item["id"],
                    "product_title": truncated_title,
                    "product_image": item["thumbnail"].replace("I.jpg", "W.jpg"),
                    "product_price": item["price"]
                }
                result.append(format_dict)
            
            return result
        except Exception as e:
                raise e

    def _truncated_text(self, max_text_length: int, text: str) -> str:
        """
        Retorna uma versão truncada do texto fornecido, limitada ao comprimento máximo especificado.

        Args: max_text_length: O comprimento máximo do texto truncado.
              text: O texto a ser truncado.
              
        Retorna: Uma versão truncada do texto, seguida de "..." se o texto original exceder o comprimento máximo, 
        caso contrário, o texto original é retornado sem modificações.
        """
        result: str = text[:max_text_length] + "..." if len(text) > max_text_length else text

        return result

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
        
    def get_products_by_category(self, category: str) -> list:
        """
        Obtémos produtos disponíveis da API externa de acordo com sua categoria e os organiza.

        Args: category: uma categoria do tipo 'str' que será usada como parametro na url da api externa.
        Retorna: Uma lista de dicionários representando os produtos organizados e formatados.
        """
        try:
            data_products: list = self._get_data_from_meliapi_by_category(category=category)

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
        
    def delete_cart_product(self, product_id: str) -> bool:
        """
        Deleta um item do carrinho com base no id do produto.

        Args:
            product_id: O ID do item a ser deletado.

        Retorna:
            bool: True se o item foi deletado com sucesso, False se o produto não foi encontrado.
        """
        try: 
            initial_count = len(self.shopping_cart)
            self.shopping_cart = [item for item in self.shopping_cart if item.product_id != product_id]

            result: bool = len(self.shopping_cart) < initial_count

            return result

        except Exception as e:
                raise e