class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        dish_info = self.menu.get(dish_name)
        if not dish_info:
            return "Dish not available"

        price = dish_info['price']
        available_quantity = dish_info['quantity']

        if quantity > available_quantity:
            return "Requested quantity not available"

        total_cost = price * quantity
        available_quantity -= quantity
        dish_info['quantity'] = available_quantity

        return total_cost


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))
print(mc.order('burger', 15))
print(mc.order('soup', 5))