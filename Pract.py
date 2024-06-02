import random 
import string 
 
def generate_password(length): 
    # Создаем список всех символов, которые могут быть использованы в пароле 
    characters = string.ascii_letters + string.digits + string.punctuation 
 
    # Генерируем пароль заданной длины 
    password = ''.join(random.choice(characters) for _ in range(length)) 
    return password 
 
# Запрашиваем у пользователя длину пароля 
length = int(input("Введите длину пароля: ")) 
 
# Генерируем пароль и выводим его 
password = generate_password(length) 
print("Сгенерированный пароль:", password)