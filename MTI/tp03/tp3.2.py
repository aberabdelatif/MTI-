class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self):
        return self.price


class VIPDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.8   # 20% de réduction


class ProDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.9   # 10% de réduction


if __name__ == '__main__':
    price = 1000

    # Client VIP
    vip = VIPDiscount(price)
    print(f"Client de type VIP → Prix après réduction : {vip.apply_discount()} DA")

    # Client professionnel
    pro = ProDiscount(price)
    print(f"Client de type PRO → Prix après réduction : {pro.apply_discount()} DA")

    # Client normal (pas de réduction)
    normal = Discount(price)
    print(f"Client normal → Prix sans réduction : {normal.apply_discount()} DA")
 