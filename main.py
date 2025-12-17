class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return self.name + ": " + str(self.price) + " руб."


class Order:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_product(self, product):
        self.items.append(product)
        self.total_cost = self.total_cost + product.price

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                self.total_cost = self.total_cost - product.price
                return

    def print_receipt(self):
        print("Чек:")
        for product in self.items:
            print(product.get_info())
        print("Итого:", self.total_cost, "руб.")


# пример работы
p1 = Product("Хлеб", 50)
p2 = Product("Молоко", 90)

order = Order()
order.add_product(p1)
order.add_product(p2)

order.remove_product("Молоко")
order.print_receipt()
