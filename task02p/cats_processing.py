from task02p.data import load_data, parse_data


def get_cats_info(file: str) -> tuple:
    rows = load_data(file)
    cats=[]
    if (rows):
        cats_data_raw = parse_data(rows)
        for cat_info_raw in cats_data_raw:
            cats.append({'id':cat_info_raw[0],'name':cat_info_raw[1],'age':cat_info_raw[2]})
    return cats
