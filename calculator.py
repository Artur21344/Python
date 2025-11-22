from unittest import result


print("Вітаю в калькуляторі!")
name = input("Як тебе звати? ")
print(f"Радий познайомитись, {name}!")
print('мій калькулятор допоможе тобі з простими обчисленнями')
num1 = int(input("Введи перше число: "))
while True:
    if num1 >= 0:
        break
    else:
        print("Будь ласка, введи додатнє число.")
        num1 = int(input("Введи перше число: "))
num2 = int(input("Введи друге число: "))
while True:
    if num2 >= 0:
        break
    else:
        print("Будь ласка, введи додатнє число.")
        num2 = int(input("Введи друге число: "))
operation = input("Введи операцію (+, -, *, /, **): ")

def plus(a, b):
    return a + b
result = plus(num1, num2)
def minus(a, b):
    return a - b
result = minus(num1, num2)
def multiply(a, b):
    return a * b
result = multiply(num1, num2)
def divide (a, b):
    return a / b
result = divide(num1, num2)
def square(a, b):
    return a ** b
result = square(num1, num2)
def invalid_operation():    
    result = "Невідома операція"

print(f"Результат: {result}")
print("Дякую, що скористався моїм калькулятором, до побачення!")

