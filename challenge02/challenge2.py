
rosseta = {'#':lambda accum,x: (accum, x + 1),
           '@':lambda accum,x: (accum, x - 1),
           '*':lambda accum,x: (accum,x**2),
           '&':lambda accum,x: (accum + str(x), x)}
def open_file(text_file: str) -> str:
    with open(text_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
def decoder(file:str):
    code = '&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&'
    start = 0
    message = ''
    for char in code:
        message, start=rosseta[char](message, start)
        print(char, start, message)
    return message
print(decoder('message_02.txt'))

    
    
    