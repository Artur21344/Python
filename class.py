class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не може бути від'ємним")
            return
        self.__balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            print("Сума для внесення має бути більшою за 0")
            return self.__balance
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Сума для зняття має бути більшою за 0")
            return self.__balance
        if amount > self.__balance:
            print("Недостатньо коштів")
            return self.__balance
        self.__balance -= amount
        return self.__balance
    
    def display_info(self):
        return f"Ім'я: {self.name}, Баланс: {self.__balance}"


Artur = Bank("Artur", 1000)
print(Artur.display_info())

withdraw = int(input("Введи суму для зняття: "))
Artur.withdraw(withdraw)
print(f"Новий баланс після зняття: {Artur.balance}")

deposit = int(input("Введи суму для внесення: "))
Artur.deposit(deposit)
print(f"Новий баланс після внесення: {Artur.balance}")