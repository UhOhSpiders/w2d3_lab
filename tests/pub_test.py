import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.guiness = Drink("Guiness", 4.50, 30)
        self.shandy = Drink("Shandy", 3.50, 20)
        self.drinks = [self.guiness, self.shandy]
        self.pub = Pub("The Thirsty Badger", 100.00)
        self.deborah = Customer("Deborah", 35.00, 57, 50)
        self.tiny_tim = Customer("Tiny Tim", 5.00, 8, 40)
        # self.pub.add_stock(self.guiness)
        # self.pub.add_stock(self.shandy)

    def test_pub_has_name(self):
        self.assertEqual("The Thirsty Badger", self.pub.name)

    def test_add_stock(self):
        self.drinks = [self.guiness, self.shandy]
        self.pub.add_stock(self.drinks)
        self.assertEqual(2, len(self.pub.drinks))

    # def test_pub_has_till_value(self):
    #     self.assertEqual(100.00, self.pub.till)

    def test_sell_drink(self):
        self.customer = self.deborah
        self.pub.sell_drink(self.customer, self.guiness)
        self.assertEqual(104.50, self.pub.till)
    
    def test_customer_spends_result(self):
        self.customer = self.deborah
        self.pub.sell_drink(self.customer, self.guiness)
        self.assertEqual(30.50, self.customer.wallet)

    def test_check_age(self):
        # self.customer = self.tiny_tim
        result = self.pub.check_age(self.tiny_tim)
        self.assertEqual(False, result)
       
    def test_check_sale_tiny_tim(self):
        self.pub.sell_drink(self.tiny_tim, self.guiness)
        self.assertEqual(5.00, self.tiny_tim.wallet)
    
    def test_check_sale_sober_deborah(self):
        self.pub.sell_drink(self.deborah, self.guiness)
        self.assertEqual(30.50, self.deborah.wallet)
    
    def test_check_sale_drunk_deborah(self):
        self.deborah.drunkenness = 70
        self.pub.sell_drink(self.deborah, self.guiness)
        self.assertEqual(35, self.deborah.wallet)
    
    
    # def test_get_stock_count(self):
    #     self.get_stock_count()
    #     self.assertEqual(2, count)

    # def test_increase_till(self):
    #     self.pub.increase_till(2.50)
    #     self.assertEqual(102.50, self.pub.till)

    # def test_add_stock