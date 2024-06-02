import random
import string

def generate_password(length):
    if length < 8:
        print("Длина пароля должна быть не менее 8 символов.")
        return None
    # Создаем список всех символов, которые могут быть использованы в пароле
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль заданной длины
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Запрашиваем у пользователя длину пароля
length = int(input("Введите длину пароля: "))

# Генерируем пароль и выводим его
password = generate_password(length)
if password is not None:
    print("Сгенерированный пароль:", password)