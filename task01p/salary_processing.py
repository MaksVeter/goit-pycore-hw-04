from task01p.data import load_data, parse_data


def total_salary(file: str) -> tuple:
    rows = load_data(file)
    total = 0
    average = 0
    if (rows):
        salaries = parse_data(rows)
        if (salaries):
            total = int(sum(salaries))
            average = int(total/len(salaries))
    return total, average
