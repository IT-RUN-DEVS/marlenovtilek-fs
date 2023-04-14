from os import path
import shutil

# Функция перемещения файла
def move_file():
    src_file = input("Введите директория перемещаемого файла:")
    dst_file = input("Введите директорию куда должен перемещаться файл:")
    if path.exists(src_file):
        new_location = shutil.move(src_file, dst_file)
        print(f'{src_file} перемещен в указанное место {new_location}')
    else:
        print("Файл не существует")