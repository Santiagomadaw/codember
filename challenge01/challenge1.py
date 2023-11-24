from functools import reduce

def open_file(text_file: str) -> str:
    with open(text_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def count_words(list_words): 
    counted_words = dict()
    for word in list_words: 
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1
    return counted_words

def load_text(file:str):
    message = open_file(file).lower()
    counted_words = count_words(message.split())
    hidden_message =reduce(lambda accum, word:accum + word + str(counted_words[word]), counted_words)
    return hidden_message

print(load_text('message_01.txt'))
