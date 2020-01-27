import unittest
from acme import Product
from acme_report import generate_products

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        """Test explode, stealability"""
        prod = Product('Test Product', 1000, 1, 100)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertEqual(prod.stealability(), 'Very stealable!')


Names=[]
ADJETIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

for x in range (0, len(ADJETIVES)):
    for y in range (0, len(NOUNS)):
        Names.append(ADJETIVES[x] + " " + NOUNS[y])


class AcmeReportTests(unittest.TestCase):
    """Test list of length 30"""

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)
        
    def test_legal_names(self):
        product = generate_products()
        names = []
        for i in range (len(product)):
            names.append(product[i].name)
            self.assertIn(names, Names)

if __name__ == '__main__':
    unittest.main()