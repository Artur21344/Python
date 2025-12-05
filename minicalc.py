print("Вітаю у міні-калькуляторі!")
a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))
operation = input("Введи операцію (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    result = "Невідома операція"

print("Результат:", result)
print("До побачення!")