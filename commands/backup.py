import os
from os import path 
import tarfile
import datetime

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