import shutil
import os

# Функция копирования файла 
def copy_file():
    src_file = input("Введите название файла:")
    dst_file = input("Введите директорию:")
    if not os.path.exists(dst_file):
        os.makedirs(dst_file)
    shutil.copy(src_file, dst_file)
    print(f"{src_file} скопирован в {dst_file}!")

