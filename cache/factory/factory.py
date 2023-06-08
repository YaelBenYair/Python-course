from abc import ABC, abstractmethod


class Pizza(ABC):
    
    def __init__(self, toppings: tuple, crust: str, size: str):
        self.size: str = size
        self.crust: str = crust
        self.toppings: tuple = toppings

    @abstractmethod
    def bake(self):
        raise NotImplemented()

    def display_pizza_details(self):
        print(f'toppings: {self.toppings}, crust: {self.crust}, size: {self.size}')


class CheesePizza(Pizza):

    def bake(self):
        print("Baking cheese pizza")


class PepperoniPizza(Pizza):

    def bake(self):
        print("Baking pepperoni pizza")


class VeggiePizza(Pizza):

    def bake(self):
        print("Baking veggie pizza")


class MeatLoversPizza(Pizza):

    def bake(self):
        print("Baking meat lovers pizza")


class NormalPizza(Pizza):

    def bake(self):
        print("Baking regular pizza")

class PizzaFactory:
    MEAT: set = ('pepperoni', 'salami', 'chicken', 'roastbeef', 'sausage')
    CHEESE: set = ('gouda', 'mozzarella', 'cheddar', 'parmesan')

    @staticmethod
    def create_pizza(toppings: tuple, crust: str, size: str):

        meet = set(toppings).intersection(PizzaFactory.MEAT)
        cheese = set(toppings).intersection(PizzaFactory.CHEESE)

        if len(meet) >= 3:
            return MeatLoversPizza(toppings, crust, size)
        elif 'pepperoni' in toppings:
            return PepperoniPizza(toppings, crust, size)
        elif len(cheese) >= 2:
            return CheesePizza(toppings, crust, size)
        elif toppings:
            return NormalPizza(toppings, crust, size)
        else:
            return VeggiePizza(toppings, crust, size)



if __name__ == '__main__':

    pizza = PizzaFactory.create_pizza(('pepperoni', 'salami', 'mozzarella'), 'standard', 'large')
    pizza.bake()
    pizza.display_pizza_details()

    pizza = PizzaFactory.create_pizza(('salami', 'mozzarella'), 'standard', 'large')
    pizza.bake()
    pizza.display_pizza_details()

    pizza = PizzaFactory.create_pizza(('salami', 'chicken', 'roastbeef'), 'standard', 'large')
    pizza.bake()
    pizza.display_pizza_details()

    pizza = PizzaFactory.create_pizza(('gouda', 'mozzarella', 'roastbeef'), 'standard', 'large')
    pizza.bake()
    pizza.display_pizza_details()




