class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):  
        return sum(item['price'] for item in self.items)


class OrderPrinter:
    def print_order(self, order):
        print("Order details:")
        for item in order.items:
            print(f"{item['name']}: ${item['price']}")


class OrderRepository:
    def save_to_db(self, order):
        print("Saving order to database...")


if __name__ == '__main__':
    products = [
        {"name": "fruit", "price": 50},
        {"name": "vegetables", "price": 100},
        {"name": "Bread", "price": 20},
        {"name": "Meat", "price": 1000},
    ]

    
    order = Order(products)


    printer = OrderPrinter()
    printer.print_order(order)

    total = order.calculate_total()
    print(f"The total sum is: ${total}")

    
    repo = OrderRepository()
    repo.save_to_db(order)
