class InvalidFileTypeError(Exception):
    """Виняток для неправильного типу файлу"""
    pass


def upload_file(filename):
    if not filename:
        raise ValueError("Назва файлу не може бути порожньою")

    if not filename.endswith(".txt"):
        raise InvalidFileTypeError("Неправильний тип файлу. Потрібен .txt")

    print("Файл успішно завантажено")


while True:
    try:
        file_name = input("Введіть назву файлу: ")
        upload_file(file_name)
        break
    except ValueError as invalid_value:
        print(invalid_value)
    except InvalidFileTypeError as invalid_file_type:
        print(invalid_file_type)
