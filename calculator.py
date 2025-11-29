def plus(a, b):
    addit = lambda a, b: a + b
def minus(a, b):
    subtr = lambda a, b: a - b
def multiply(a, b):
    mult = lambda a, b: a * b
def divide (a, b):
    div = lambda a, b: a / b
def square(a, b):
    sqr = lambda a, b: a ** b
def invalid_operation():
    return lambda a, b: "неправильна операція"

from unittest import result
print("Вітаю в калькуляторі!")
name = input("Як тебе звати? ")
print(f"Радий познайомитись, {name}!")
print('мій калькулятор допоможе тобі з простими обчисленнями')

while True:
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
    print("Результат: ")
    if operation == '+':
        print(plus(num1, num2))
    elif operation == '-':
        print(minus(num1, num2))
    elif operation == '*':
        print(multiply(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    elif operation == '**':
        print(square(num1, num2))
    else:
        print(invalid_operation())
    print("Дякую, що скористався моїм калькулятором, до побачення!")

    answer = input("Хочеш зробити ще одне обчислення? (так/ні): ")
    if answer == 'так':
        continue
    elif answer != 'так' and answer != 'ні':
        print("операція невірна")
    elif answer == 'ні':
        print("До побачення!")
    break
      