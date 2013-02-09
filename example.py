# tests.py
import unittest
from ddt import ddt, data, data_provider

class DataProviders(object):
	def larger_then_two(self, count=4):
		return [3, 4, 5, 6, 7, 8][0:count]
_data_providers = DataProviders()

@ddt
class FooTestCase(unittest.TestCase):

	@data(3, 4, 5, 6)
	def test_data_annotation(self, value):
		self.assertTrue(value > 2)

	@data_provider(_data_providers.larger_then_two, 2)
	def test_data_provider_annotation(self, value):
		self.assertTrue(value > 2)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(FooTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)