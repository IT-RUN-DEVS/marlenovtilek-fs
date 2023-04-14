import os

# Функция инициализации новой файловой системы
def init():
    new_directory = input("Дайте название для новой директории: ")
    path = os.path.join(new_directory)
    os.makedirs(path)
    print(f"Директрия {new_directory} успешно создалась!")