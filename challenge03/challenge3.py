import re
from functools import reduce

def decoder(file: str, number:int):
    with open(file, 'r', encoding='utf-8') as file: content_list = file.read().split('\n')
    splited_codes = map(lambda code: re.split(r'[-\s:]+', code), content_list)
    corrupted_codes = list(filter(lambda code:    not (int(code[0]) <= code[3].count(code[2]) <= int(code[1])) , splited_codes))
    
    
    return corrupted_codes[number-1][3]

print(decoder('encryption_policies.txt', 42))
