from task02p import get_cats_info


def main():
    file = './resources/task02/cats.txt'
    cats_info = get_cats_info(file)
    print(cats_info)


if __name__ == "__main__":
    main()
