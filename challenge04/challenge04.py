def format_file(file_name):
    splited_name = file_name.split('-')
    no_repeated = (splited_name[0])
    print
    for index in range(len(splited_name[0])):
        
        if splited_name[0][index] in splited_name[0][index+1:] and splited_name[0][index] in no_repeated:
            no_repeated = no_repeated.replace(splited_name[0][index],'')
  
    return no_repeated, splited_name[1]
        

    


def checker(file):
    with open(file,'r') as raw_file_list:
        file_list = raw_file_list.read().split('\n')
    index = 0
    for file_name in file_list:
        check, checksum = format_file(file_name)
        
        if check == checksum:
            index +=1
       
        if index == 33:
            return check
        
        
print(checker('files_quarantine.txt'))      