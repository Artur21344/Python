add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
sqrt = lambda a, b: a ** b
def invalid_operation():
    return lambda: "Операція невірна"
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
        print(add(num1, num2))
    elif operation == '-':
        print(sub(num1, num2))
    elif operation == '*':
        print(mul(num1, num2))
    elif operation == '/':
        print(div(num1, num2))
    elif operation == '**':
        print(sqrt(num1, num2))
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
      