import re


def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.readlines()
    except:
        print(f'Read file {filename} error')


def clear_value(val) -> str:
    return re.sub(r'\W', '', val)


def parse_data(data: list) -> list:
    res = []
    for row in data:
        try:
            res.append([clear_value(val) for val in row.split(',')])
        except:
            print('Data parse error')
            break
    return res
