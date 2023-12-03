import re


def is_corrupted(code):
    return not (int(code[0]) <= code[3].count(code[2]) <= int(code[1]))


def open_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        content_list = file.read().split('\n')
    return content_list


def decoder(file: str, number: int):

    content_list = open_file(file)

    splited_codes = map(lambda code: re.split(r'[-\s:]+', code), content_list)
    corrupted_codes = filter(lambda code: is_corrupted(code), splited_codes)
    corrupted_codes = list(corrupted_codes)
    return corrupted_codes[number-1][3]


print(decoder('encryption_policies.txt', 42))
