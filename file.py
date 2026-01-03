class InvalidFileTypeError(Exception):
    """Виняток для неправильного типу файлу"""
    pass


def upload_file(filename):
    if not filename:
        raise ValueError("Назва файлу не може бути порожньою")

    if not filename.endswith(".txt"):
        raise InvalidFileTypeError("Неправильний тип файлу. Потрібен .txt")

    print("Файл успішно завантажено")


try:
    file_name = input("Введіть назву файлу: ")
    upload_file(file_name)
except ValueError as неправильне_значення:
    print(неправильне_значення)
except InvalidFileTypeError as неправильний_тип_файлу:
    print(неправильний_тип_файлу)
