import sys
import json
from pprint import pprint

def process_the_test_recursively(test: dict, test_value: dict):
    "Рекурсия обработки тестов"
    if test['id'] == test_value['id']:
        test['value'] = test_value['value']
    
    if 'values' in test.keys():
        for inner_test in test['values']:
            process_the_test_recursively(inner_test, test_value)


def main(file_values: str, file_tests: str, file_report: str):
    with open(file_values, "r") as file:
        values = json.load(file)['values']

    with open(file_tests, "r") as file:
        tests = json.load(file)

    for test_value in values:
        for test in tests['tests']:
            process_the_test_recursively(test, test_value)
        
    with open(file_report, 'w') as file:
        json.dump(tests, file, indent=2)

if __name__ == '__main__':
    assert len(sys.argv) > 3, "Программа ожидает на вход три обязательных аргумента!"

    main(*sys.argv[1:4])