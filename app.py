import os
import sys
from datetime import datetime

# Путь к каталогу, который нужно анализировать
path = sys.argv[2] if len(sys.argv) > 2 else "/"

def get_file_list(directory):
    """Получить список всех файлов в указанном каталоге."""
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_list.append(filepath)
    return file_list

def get_top_files(file_list):
    """Получить топ-10 файлов по размеру."""
    files_with_size = []
    for file in file_list:
        try:
            size = os.path.getsize(file) / 1024  # Размер файла в Кб
            files_with_size.append((file, size))
        except (FileNotFoundError, PermissionError):
            # Игнорируем файлы, к которым нет доступа или которые не существуют
            continue
    sorted_files = sorted(files_with_size, key=lambda x: x[1], reverse=True)
    return sorted_files[:10]

if __name__ == "__main__":
    # Получение имени пользователя и вывод приветствия
    name = sys.argv[1] if len(sys.argv) > 1 else "User"
    print(f"Hello, {name}!")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Получение списка файлов и их подсчёт
    files = get_file_list(path)
    print(f"Total number of files: {len(files)}")

    # Вывод топ-10 файлов по размеру
    top_files = get_top_files(files)
    print("Top 10 largest files (in KB):")
    for file, size in top_files:
        print(f"{file}: {size:.2f} KB")
