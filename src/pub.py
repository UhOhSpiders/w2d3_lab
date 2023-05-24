class Pub():
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, new_sale_value):
        self.till += new_sale_value

    # def get_till(self):
    #     return self.till

   
    
    def add_stock(self, drinks):
        for drink in drinks:
            self.drinks.append(drink)

    def check_drunkenness(self, customer):
        if customer.drunkenness < 60:
            return True
    
    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    
    def sell_drink(self, customer, drink):
        if self.check_drunkenness(customer) and self.check_age(customer):
            self.increase_till(drink.price)
            customer.spend(drink.price)
   
   
   
    # def get_stock_count(self):
    #     count = len(self.drinks)
    #     return count
