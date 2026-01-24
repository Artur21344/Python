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
filtered_expenses = [expense for expense in expenses if expense > 100]
print("Витрати більші за 100:", filtered_expenses)
sumed_expenses = [int(expense * 1.1) for expense in expenses]
print("Витрати збільшені на 10%:", sumed_expenses)