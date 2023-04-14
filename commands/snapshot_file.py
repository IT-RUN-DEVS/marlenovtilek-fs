import shutil
import tarfile
import os

# Функция создания снимки файловой системы
def snapshot():
    snapshot_copy_name = input("Введите название для snapshot: ")
    snapshot_copy_path = os.path.join(f"{snapshot_copy_name}")
    shutil.make_archive(snapshot_copy_path,'zip')
    print(f"SnapShot {snapshot_copy_name} успешно создан")
