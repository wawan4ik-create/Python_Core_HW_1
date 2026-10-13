"""Ітерація вкладень у директорії та вивід її вмісту у вигляді дерева з кольоровим виділенням директорій та файлів.
Директорії виділяються синім кольором, а файли - зеленим.
Використання python task3.py <шлях_до_директорії> для запуску скрипта."""
import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def iter_dir(path: Path, level: int = 0):
    """Ітерація по директорії та вивід її вмісту у вигляді дерева. 
        param path: Шлях до директорії
        param level: Рівень вкладеності директорії"""
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))  # Спочатку папки
    except PermissionError:
        print('    ' * level + Fore.RED + 'Permission denied: ' + path.name)
        return
            
    for item in items:
        if item.is_dir():
            print('    ' * level + Fore.BLUE + item.name)
            iter_dir(item, level + 1)
        else:
            print('    ' * level + Fore.GREEN + item.name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a path to the directory.")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print("The provided path does not exist.")
        sys.exit(1)
    if not path.is_dir():
        print("The provided path is not a directory.")
        sys.exit(1)

    iter_dir(path)