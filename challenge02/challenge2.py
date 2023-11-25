from functools import reduce

rosseta = {'#': lambda x: (x[0], x[1] + 1),
           '@': lambda x: (x[0], x[1] - 1),
           '*': lambda x: (x[0], x[1] **2),
           '&': lambda x: (x[0] + str(x[1]), x[1])}


def decoder(file: str):
    with open(file, 'r', encoding='utf-8') as file:
        return reduce(lambda accum, char: rosseta[char](accum), file.read(), ('', 0))[0]

print(decoder('message_02.txt'))
