import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(input_data):
    print(json.dumps(input_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data(input('Enter the filepath: ')))
