def reverse_with_loop(text):
    """Перевертає рядок за допомогою циклу"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


def reverse_with_slice(text):
    """Виводить оригінальний рядок за допомогою зрізу"""
    return text[::]


user_input = input("Введіть рядок: ")

result_loop = reverse_with_loop(user_input)

result_slice = reverse_with_slice(user_input)

print("\n--- Результати ---")
print(f"Перевернутий (цикл): {result_loop}")
print(f"Оригінальний: {result_slice}")