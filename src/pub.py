class Pub():
    def __init__(self, name, till, stock):
        self.name = name
        self.till = till
        self.stock = stock
        self.drinks = []
        

    def increase_till(self, new_sale_value):
        self.till += new_sale_value

    # def get_till(self):
    #     return self.till

    def stock_value(self):
        value = 0
        for ammount in self.stock:
            
            value += 
        
        return self.stock
    
    def add_stock(self, drinks):
        for drink in drinks:
            self.drinks.append(drink)

    def check_drunkenness(self, customer):
        if customer.drunkenness < 60:
            return True
        else:
            return False
    
    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    
    def sell_drink(self, customer, drink):
        if self.check_drunkenness(customer) and self.check_age(customer):
            self.increase_till(drink.price)
            customer.spend(drink.price)

    def sell_food(self, customer, food):
            self.increase_till(food.price)
            customer.spend(food.price)
            customer.drunkenness -= food.rejuvenation_level
   
   
   
   
    # def get_stock_count(self):
    #     count = len(self.drinks)
    #     return count
