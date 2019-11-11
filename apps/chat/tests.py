from django.test import TestCase
from apps.chat.language_validator import valid_language
from apps.chat.stocks import get_stock_price

# Create your tests here.

class LanguageValidatorTest(TestCase):

	def test_language(self):
		aleman = 'Güten mörgen'
		espanol = 'Buenos días'
		italiano = 'Buongiorno'
		ingles = 'Good morning'
		self.assertEqual(valid_language(aleman), False)
		self.assertEqual(valid_language(espanol), True)
		self.assertEqual(valid_language(italiano), False)
		self.assertEqual(valid_language(ingles), False)

	def test_faang_stocks(self):
		facebook = 'FB.US'
		apple = 'AAPL.US'
		amazon = 'AMZN.US'
		netflix = 'NFLX.US'
		google = 'GOOG.US'
		self.assertEqual(facebook in get_stock_price(1, facebook), True)
		self.assertEqual(apple in get_stock_price(1, apple), True)
		self.assertEqual(amazon in get_stock_price(1, amazon), True)
		self.assertEqual(netflix in get_stock_price(1, netflix), True)
		self.assertEqual(google in get_stock_price(1, google), True)