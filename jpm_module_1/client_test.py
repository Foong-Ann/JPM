import unittest
from client import *

##test getDataPoint
class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

##test getRatio
  def test_getRatio_price_b_notZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    price_a= (quotes[0]['top_bid']['price']+quotes[0]['top_ask']['price'])/2
    price_b= (quotes[1]['top_bid']['price']+quotes[1]['top_ask']['price'])/2
    self.assertEqual(getRatio(price_a,price_b), price_a/price_b)

  def test_getRatio_price_b_isZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    price_a= (quotes[0]['top_bid']['price']+quotes[0]['top_ask']['price'])/2
    price_b= (quotes[1]['top_bid']['price']+quotes[1]['top_ask']['price'])/2
    if (price_b==0):
      return
    self.assertEqual(getRatio(price_a,price_b), price_a/price_b)
    
    def test_getRatio_priceBZero(self):
     price_a = 119.2
     price_b = 0
     self.assertIsNone(getRatio(price_a, price_b))
 
   def test_getRatio_priceAZero(self):
     price_a = 0
     price_b = 121.68
     self.assertEqual(getRatio(price_a, price_b), 0)
 
   def test_getRatio_greaterThan1(self):
     price_a = 346.48
     price_b = 166.39
     self.assertGreater(getRatio(price_a, price_b), 1)
 
   def test_getRatio_LessThan1(self):
     price_a = 166.39
     price_b = 356.48
     self.assertLess(getRatio(price_a, price_b), 1)
 
   def test_getRatio_exactlyOne(self):
     price_a = 356.48
     price_b = 356.48
     self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
