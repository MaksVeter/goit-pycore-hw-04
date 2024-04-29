import sys
from pathlib import Path
from colorama import Fore, Style


def main():
    if (len(sys.argv) > 1):
        path = Path(sys.argv[1])
        if (path.is_dir()):
            print_dir_structure(path)
            print(Style.RESET_ALL)
        else:
            print('Wrong path')


def print_dir_structure(path, indent=''):
    path = Path(path)
    if path.is_file():
        print(Fore.YELLOW+indent+path.name)
    elif path.is_dir():
        print(Fore.BLUE+indent+path.name)
        for item in path.iterdir():
            print_dir_structure(item, indent+'  ')


if __name__ == "__main__":
    main()
