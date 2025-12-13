class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів")
        self.balance -= amount
        return self.balance
        
    def display_info(self):
        print(f"Ім'я: {self.name}, Баланс: {self.balance}")

Artur = Bank("Artur", 1000)
Artur.display_info()

withdraw = input("Введи суму для зняття: ")
Artur.withdraw(int(withdraw))
if int(withdraw) <= Artur.balance:
    print(f"Новий баланс після зняття: {Artur.balance}")


deposit = input("Введи суму для внесення: ")
Artur.deposit(int(deposit))
print(f"Новий баланс після внесення: {Artur.balance}")