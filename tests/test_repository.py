import unittest
from src.repository import RepositoryShoppingCart

class Product:
    def __init__(self, product_id, product_title, product_image, product_price):
        self.product_id = product_id
        self.product_title = product_title
        self.product_image = product_image
        self.product_price = product_price

class TestRepositoryShoppingCart(unittest.TestCase):
    def setUp(self):
        self.repository = RepositoryShoppingCart()
        self.products_list = [
            {'id': 'ID_1', 'title': 'Product 1', 'thumbnail': 'image1_I.jpg', 'price': 10.0},
            {'id': 'ID_2', 'title': 'Product 2', 'thumbnail': 'image2_I.jpg', 'price': 20.0},
            {'id': 'ID_3', 'title': 'Product 3', 'thumbnail': 'image3_I.jpg', 'price': 30.0}
        ]
        self.format_products_list = [
            Product('ID_1', 'Product 1', 'image1_W.jpg', 10.0),
            Product('ID_2', 'Product 2', 'image2_W.jpg', 20.0),
            Product('ID_3', 'Product 3', 'image3_W.jpg', 30.0)
        ]

    def test_organize_products_list(self):
        """
        Testa o método _organize_products_list e verifica se a lista de produtos é organizada corretamente conforme esperado.
        """
        result = self.repository._organize_products_list(self.products_list)
        expected_result = [
            {
                "product_id": 'ID_1',
                "product_title": 'Product 1',
                "product_image": 'image1_W.jpg',
                "product_price": 10.0
            },
            {
                "product_id": 'ID_2',
                "product_title": 'Product 2',
                "product_image": 'image2_W.jpg',
                "product_price": 20.0
            },
            {
                "product_id": 'ID_3',
                "product_title": 'Product 3',
                "product_image": 'image3_W.jpg',
                "product_price": 30.0
            }
        ]

        self.assertEqual(result, expected_result)

    def test_post_cart_products(self):
        """
        Testa o método post_cart_products e verifica se os produtos são adicionados corretamente ao carrinho.
        """
        result = self.repository.post_cart_products(self.format_products_list)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].product_id, 'ID_1')
        self.assertEqual(result[1].product_id, 'ID_2')

        self.assertEqual(len(self.repository.shopping_cart), 3)
        self.repository.shopping_cart.clear()
        self.assertEqual(len(self.repository.shopping_cart), 0)

    def test_get_cart_products(self):
        """
        Testa o método get_cart_products e verifica se os produtos do carrinho são retornados corretamente.
        """
        self.repository.shopping_cart = self.format_products_list

        result = self.repository.get_cart_products()

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].product_id, 'ID_1')
        self.assertEqual(result[1].product_id, 'ID_2')

    def test_truncated_text(self):
        """
        Testa o método _truncated_text e se necessário de acordo com os parâmetros, reduz a quantidade de caracteres do texto.
        """
        max_length = 10

        long_text = "This is a longer text than the maximum length"
        long_text_expected_result = "This is a ..."

        short_text = "Short text"
        short_text_expected_result = "Short text"

        long_text_result = self.repository._truncated_text(max_length, long_text)
        self.assertEqual(long_text_result, long_text_expected_result)

        short_text_result = self.repository._truncated_text(max_length, short_text)
        self.assertEqual(short_text_result, short_text_expected_result)

    def test_delete_cart_product_success(self):
        """
        Testa o método delete_cart_product para verificar se um produto é deletado corretamente.
        """
        self.repository.shopping_cart = self.format_products_list
        result = self.repository.delete_cart_product('ID_1')
        self.assertTrue(result)
        self.assertEqual(len(self.repository.shopping_cart), 2)
        self.assertNotIn(
            next((item for item in self.repository.shopping_cart if item.product_id == 'ID_1'), None),
            self.repository.shopping_cart
        )

    def test_delete_cart_product_not_found(self):
        """
        Testa o método delete_cart_product para verificar a tentativa de deletar um produto que não está no carrinho.
        """
        self.repository.shopping_cart = self.format_products_list
        result = self.repository.delete_cart_product('ID_4')
        self.assertFalse(result)
        self.assertEqual(len(self.repository.shopping_cart), 3)

if __name__ == '__main__':
    unittest.main()
