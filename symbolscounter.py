user_input = input("Введіть рядок: ")

length = 0
letters = 0
digits = 0
other = 0

for char in user_input:
    length += 1
    
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        other += 1

print("\n--- Результати ---")
print(f"Довжина рядка: {length}")
print(f"Літер: {letters}")
print(f"Цифр: {digits}")
print(f"Інших символів: {other}")