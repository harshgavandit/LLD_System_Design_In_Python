from chef import Chef
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

chef = Chef()
burgerOrder = BurgerOrder(chef)
pizzaOrder = PizzaOrder(chef)

waiter = Waiter()
waiter.take_order(burgerOrder)
