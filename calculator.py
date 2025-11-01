print("Вітаю в калькуляторі!")
name = input("Як тебе звати? ")
print(f"Радий познайомитись, {name}!")
print('мій калькулятор допоможе тобі з простими обчисленнями')
num1 = int(input("Введи перше число: "))
num2 = int(input("Введи друге число: "))
operation = input("Введи операцію (+, -, *, /, **): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '**':
    result = num1 ** num2
else:
    result = "Невідома операція"
while True:
    print("Бажаєш виконати ще одну операцію?")
    again = input("Введи 'так' для продовження або 'ні' для виходу: ").lower()
    if again == 'так':
        num1 = int(input("Введи перше число: "))
        num2 = int(input("Введи друге число: "))
        operation = input("Введи операцію (+, -, *, /, **): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        else:
            result = "Невідома операція"
    elif again == 'ні':
        break
print(f"Результат: {result}")
print("Дякую, що скористався моїм калькулятором, до побачення!")

