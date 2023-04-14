import os
import shutil
from os import path 
import tarfile
import datetime

# Функция создания нового файла
def create_file():
    file_name = input("Введите название файла:")
    file_path = os.path.join(file_name)
    if os.path.exists(file_path):
        print(f"Файл {file_name} уже существует.")
    else:
        with open(file_path, 'w+') as f: 
            print(f"Файл {file_name} создан!") 

# Функция вывода списка файлов и директорий 
def get_file(dir_path):
    dir_path = input("Введите название директорий:")
    files_and_dirs = os.listdir(dir_path)
    if files_and_dirs:
        print("Файлы и директорий:")
        for item in files_and_dirs:
            print(item)
    else:
        print("Папка пуста!")

# Функция копирования файла 
def copy_file():
    src_file = input("Введите название файла:")
    dst_file = input("Введите директорию:")
    if not os.path.exists(dst_file):
        os.makedirs(dst_file)
    shutil.copy(src_file, dst_file)
    print(f"{src_file} скопирован в {dst_file}!")
    

# Функция перемещения файла 
def move_file():
    src_file = input("Введите директория перемещаемого файла:")
    dst_file = input("Введите директорию куда должен перемещаться файл:")
    if path.exists(src_file):
        new_location = shutil.move(src_file, dst_file)
        print(f'{src_file} перемещен в указанное место {new_location}')
    else:
        print("Файл не существует")

# Функция инициализации новой файловой системы
def init():
    new_directory = input("Дайте название для новой директории: ")
    path = os.path.join(new_directory)
    os.makedirs(path)
    print(f"Директрия {new_directory} успешно создалась!")

# Функция создания снимки файловой системы
def snapshot():
    snapshot_copy_name = input("Введите название для snapshot: ")
    snapshot_copy_path = os.path.join(f"{snapshot_copy_name}")
    shutil.make_archive(snapshot_copy_path,'zip')
    print(f"SnapShot {snapshot_copy_name} успешно создан")


# Функция создания резервной копии файловой системы
def backup():
    src_dir = input("Введите директорию файла:")
    dest_dir = input("Введите директорию:")
    now = datetime.datetime.now()
    file_new_name = input("Введите название новой резервной копии:")
    backup_name = now.strftime("%d-%m-%y") + " " + file_new_name + ".tar.gz"
    dest_file = os.path.join(dest_dir, backup_name)
    with tarfile.open(dest_file, 'w:gz') as tar:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                tar.add(dir_path)
    print("Резервная копия создана:", dest_file)



if __name__ == "__main__":

    while True:
    # Проверка на команды
        commands = input("Выберите команду: create, list, copy, move, init, snapshot, backup, exit : ")
        if commands == "create":
            create_file()
        elif commands == "list":
            get_file(dir_path=None)
        elif commands == "copy":
            copy_file()
        elif commands == "move":
            move_file()
        elif commands == "init":
            init()
        elif commands == "snapshot":
            snapshot()
        elif commands == "backup":
            backup()
        elif commands == "exit":
            break
        else:
            print("Введите верную команду!")
        