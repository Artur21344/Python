class Product:
    tax_procent = 19  

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def price_with_tax(price):
        return price + price * Product.tax_procent / 100

    def __str__(self):
        return f"Товар: {self.name}, ціна: {self.price}"

    def __add__(self, other):
        total_price = self.price + other.price
        return Product.price_with_tax(total_price)

product1 = Product("Хліб", 30)
product2 = Product("Молоко", 40)
product3 = Product("Яйця", 20)


print(product1)
print(product2)
print(product3)

result = product1 + product2 + product3
print("Загальна вартість з податком:", result)