from slugify import slugify
from functools import reduce


def analizer(file):
    with open(file, 'r') as raw_list:
        listofdata = raw_list.read().split('\n')
    list_ok = list(map(lambda line: line.split(','), listofdata))
    id_ok = filter(lambda line: line[0].lower() != '' and line[0].lower() == slugify(line[0]), list_ok)

    name_ok = filter(lambda line: line[1].lower() == slugify(line[1]), id_ok)

    mail_ok = filter(lambda line:   ('@' in line[2] and len(line[2].split('@')) == 2 and
                                    line[2].split('@')[0] != '' and
                                    '.' in line[2].split('@')[1] and
                                    len(line[2].split('@')[1].split('.')) == 2),
                                    name_ok)
    
    age_ok = filter(lambda line: line[3].lower().isdigit() or line[3].lower() == '', mail_ok)
    
    address_ok = list(filter(lambda line: type(line[4].lower()) == str or line[4].lower() == '', age_ok))
    
    bad_list = filter(lambda x: x not in address_ok, list_ok)
    
    origin_list = list(list_ok)
    
    code = reduce(lambda accum, x: accum + x[1][0] if x[1] != '' else accum, bad_list, '')
    return code


print(analizer('database_attacked.txt'))
