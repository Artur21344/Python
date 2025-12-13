def sum_of_numbers(*numbers):
    total = 0
    for i in numbers:
        total += float(i)
    return total
print(f"Сума дорівнює: {sum_of_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")