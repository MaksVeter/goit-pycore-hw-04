from task01p import total_salary


def main():
    file = './resources/task01/salaries.txt'
    total, average = total_salary(file)
    print(f"Загальна сума заробітної плати: {
          total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()
