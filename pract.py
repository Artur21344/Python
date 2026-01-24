#Завдання: Аналіз витрат за тиждень
#Є список витрат за тиждень (числа).
#Потрібно:Вивести всі витрати.Знайти мінімальну та максимальну витрату.
# Порахувати загальну суму.Відсортувати витрати за зростанням.Вивести тільки ті витрати, які більші за 100.
# Збільшити всі витрати на 10% (новий список).


expenses = [
    1200,
    350,
    4999,
    870,
    150,
    2300,
    75,
    980,
    4100,
    600,
    250,
    1300,
    5200,
    90,
    760,
    1800,
    45,
    999,
    3100,
    400,
]
expenses.sort()
print("Всі витрати за тиждень:", expenses)
min_expense = min(expenses)
max_expense = max(expenses)
total_expense = sum(expenses)
print("Мінімальна витрата:", min_expense)
print("Максимальна витрата:", max_expense)
print("Загальна сума витрат:", total_expense)
more100_expenses = list(filter(lambda x: x > 100, expenses)) 
print("Витрати більші за 100:", more100_expenses)
sumed_expenses = list(map(lambda x: int(x * 1.1), expenses))
print("Витрати збільшені на 10%:", sumed_expenses)