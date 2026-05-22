from discount_strategy import DiscountStrategy


class DiwaliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying diwali discount of 20%")
