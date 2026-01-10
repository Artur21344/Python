def check_password_strength(password):
    has_length = len(password) > 8
    
    has_letter = any(char.isalpha() for char in password)
    
    has_digit = any(char.isdigit() for char in password)
    
    is_strong = has_length and has_letter and has_digit
    
    return is_strong, has_length, has_letter, has_digit


def main():
    
    password = input("\nВведіть пароль для перевірки: ")
    
    is_strong, has_length, has_letter, has_digit = check_password_strength(password)

    print("РЕЗУЛЬТАТИ ПЕРЕВІРКИ:")
    
    print(f" Довжина більше 8 символів: {'ТАК' if has_length else 'НІ'} (поточна довжина: {len(password)})")
    print(f" Містить хоча б 1 літеру: {'ТАК' if has_letter else 'НІ'}")
    print(f" Містить хоча б 1 цифру: {'ТАК' if has_digit else 'НІ'}")
    
    if is_strong:
        print(" ПАРОЛЬ НАДІЙНИЙ!")
    else:
        print(" ПАРОЛЬ НЕНАДІЙНИЙ!")
        print("\nДля підвищення надійності:")
        if not has_length:
            print("  - Використайте більше 8 символів")
        if not has_letter:
            print("  - Додайте хоча б одну літеру")
        if not has_digit:
            print("  - Додайте хоча б одну цифру")

if __name__ == "__main__":
    main()