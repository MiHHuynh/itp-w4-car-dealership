class Vehicle(object):
    
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.sale_multiplier
    
    def purchase_price(self):
        return self.sale_price() - (self.purchase_multiplier * self.miles)

class Car(Vehicle):
    
    def __init__(self, **kwargs):
        Vehicle.__init__(self, **kwargs)
        self.sale_multiplier = 1.2
        self.purchase_multiplier = 0.004

class Motorcycle(Vehicle):
    
    def __init__(self, **kwargs):
        Vehicle.__init__(self, **kwargs)
        self.sale_multiplier = 1.1
        self.purchase_multiplier = 0.009


class Truck(Vehicle):
    
    def __init__(self, **kwargs):
        Vehicle.__init__(self, **kwargs)
        self.sale_multiplier = 1.6
        self.purchase_multiplier = 0.02
