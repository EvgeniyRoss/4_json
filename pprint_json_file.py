import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_file:
        input_data = json.load(json_file)
    return input_data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data(r'''C:\Users\Ползователь\4_json\alco_shops.json'''))
