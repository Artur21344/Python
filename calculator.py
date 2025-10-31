print("Вітаю в калькуляторі!")
name = input("Як тебе звати? ")
print(f"Радий познайомитись, {name}!")
print('мій калькулятор допоможе тобі з простими обчисленнями')
num1 = int(input("Введи перше число: "))
num2 = int(input("Введи друге число: "))
operation = input("Введи операцію (+, -, *, /, **): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Невідома операція"

print(f"Результат: {result}")

while True:
    again = input("Бажаєш виконати ще одну операцію? (так/ні): ").lower()
    if again == "так":
        num1 = int(input("Введи перше число: "))
        num2 = int(input("Введи друге число: "))
        operation = input("Введи операцію (+, -, *, /, **): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Невідома операція"

        print(f"Результат: {result}")
    elif again == "ні":
        print(f"До побачення, {name}!")
        break
    else:
        print("Будь ласка, відповідай 'так' або 'ні'.")

