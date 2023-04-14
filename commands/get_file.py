import os

# Функция вывода списка файлов и директорий (list)
def get_file(dir_path):
    dir_path = input("Введите название директорий:")
    files_and_dirs = os.listdir(dir_path)
    if files_and_dirs:
        print("Файлы и директорий:")
        for item in files_and_dirs:
            print(item)
    else:
        print("Папка пуста!")
