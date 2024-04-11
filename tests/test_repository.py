import unittest
from unittest.mock import patch, MagicMock
from src.repository import RepositoryShoppingCart


class TestRepositoryShoppingCart(unittest.TestCase):
    def setUp(self):
        self.repository = RepositoryShoppingCart()
        self.products_list = [
            {'id': 'ID_1', 'title': 'Product 1', 'thumbnail': 'image.I.jpg', 'price': 10.0},
            {'id': 'ID_2', 'title': 'Product 2', 'thumbnail': 'image2.I.jpg', 'price': 20.0},
            {'id': 'ID_3', 'title': 'Product 3', 'thumbnail': 'image3.I.jpg', 'price': 30.0}
        ]
        self.format_products_list =[
            {
                "product_id": 'ID_1',
                "product_title": 'Product 1',
                "product_image": 'image.W.jpg',
                "product_price": 10.0
            },
            {
                "product_id": 'ID_2',
                "product_title": 'Product 2',
                "product_image": 'image2.W.jpg',
                "product_price": 20.0
            },
            {
                "product_id": 'ID_3',
                "product_title": 'Product 3',
                "product_image": 'image3.W.jpg',
                "product_price": 30.0
            }
        ]

    def test_organize_products_list(self):
        result = self.repository._organize_products_list(self.products_list)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]['product_id'], 'ID_1')
        self.assertEqual(result[0]['product_title'], 'Product 1')
        self.assertEqual(result[0]['product_image'], 'image.W.jpg')
        self.assertEqual(result[0]['product_price'], 10.0)
        self.assertEqual(result, self.format_products_list)


    def test_post_cart_products(self):
        result = self.repository.post_cart_products(self.format_products_list)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]['product_id'], 'ID_1')
        self.assertEqual(result[1]['product_id'], 'ID_2')

        self.assertEqual(len(self.repository.shopping_cart), 3)
        self.repository.shopping_cart.clear()
        self.assertEqual(len(self.repository.shopping_cart), 0)


    def test_get_cart_products(self):
        self.repository.shopping_cart = self.format_products_list

        result = self.repository.get_cart_products()

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]['product_id'], 'ID_1')
        self.assertEqual(result[1]['product_id'], 'ID_2')

if __name__ == '__main__':
    unittest.main()
