import os

# Создаем новый файл (create)
def create_file():
    file_name = input("Введите название файла:")
    file_path = os.path.join(file_name)
    if os.path.exists(file_path):
        print(f"Файл {file_name} уже существует.")
    else:
        with open(file_path, 'w+') as f: 
            print(f"Файл {file_name} создан!") 
