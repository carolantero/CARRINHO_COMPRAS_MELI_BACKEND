import unittest
from fastapi import HTTPException
from src.repository import RepositoryShoppingCart

class TestRepositoryShoppingCartIntegration(unittest.TestCase):
    def setUp(self):
        self.repository = RepositoryShoppingCart()

    def assert_valid_product_list(self, product_list):

        self.assertIsInstance(product_list, list)
        self.assertGreater(len(product_list), 0)
        
        for item in product_list:
            self.assertIn('id', item)
            self.assertIn('title', item)
            self.assertIn('price', item)
            self.assertIn('thumbnail', item)

    def test_get_data_from_meliapi_valid(self):
        """
        Testa os métodos _get_data_from_meliapi e _get_data_from_meliapi_by_category que fazem integração com a api externa do Mercado Livre.
        """
        category = 'eletrodomestico'

        try:
            result_all = self.repository._get_data_from_meliapi()
            result_by_category = self.repository._get_data_from_meliapi_by_category(category)

            self.assert_valid_product_list(result_all)
            self.assert_valid_product_list(result_by_category)
                
        except HTTPException as e:
            self.fail(f"HTTPException raised: {e.detail}")


    def test_get_data_from_meliapi_by_category_invalid(self):
        """
        Testa o método _get_data_from_meliapi_by_category que faz integração com a api externa do Mercado Livre e valida se o parâmetro 'category' possui um valor válido.
        """
        category = '#########'
        
        with self.assertRaises(HTTPException) as context:
            self.repository._get_data_from_meliapi_by_category(category)

        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Categoria não é válida ou não retornou resultados. Por favor, tente outra categoria.")


if __name__ == '__main__':
    unittest.main()
