import json as js
from pprint import pprint as pp
import datetime



if __name__ == '__main__':
    DB_name = 'competitors2.json'
    with open(DB_name, 'r', encoding='utf-8') as file:
        names_DataBase = js.load(file)
        #pp(names_DataBase)
    log_name = 'results_RUN.txt'
    #print()
    log = open(log_name).readlines()
    for x in range(len(log)):
        log[x] = log[x].split()
        log[0][0] = 287
        log[x][0] = int(log[x][0])
        log[x][2] = log[x][2].split(':')
        log[x][2] = float(log[x][2][0])*3600 + float(log[x][2][1])*60 + float(log[x][2][2].replace(',', '.'))
    #pp(log)
    #print()
    number_of_lines = 598-236
    #print(number_of_lines)
    help_arr = [0 for col in range(number_of_lines)]
    #print()
    #print(help_arr)
    for counter in range(598):
        if log[counter][1] == 'start':
            #print(log[counter][0], 'started')
            help_arr[log[counter][0]] -= log[counter][2]
        else:
            #print(log[counter][0], 'finished')
            help_arr[log[counter][0]] += log[counter][2]
    #print(help_arr)
    for x in range(len(help_arr)):
        if help_arr[x] == 0:
            continue
        else:
            help_arr[x] = [x, names_DataBase[str(x)]['Name'], names_DataBase[str(x)]['Surname'], help_arr[x]]
    #print(help_arr)
    for x in range(len(help_arr)):
        if x < len(help_arr):
            #print(x)
            if help_arr[x] == 0:
                del help_arr[x]
        else:
            break
    for x in range(29):
        help_arr.remove(0)
    #pp(help_arr)
    help_arr.sort(key = lambda x: x[3])
    #pp(help_arr)
    print("занятое место нагрудный номер Имя Фамилия результат")
    for x in range(len(help_arr)):
        print(x+1, help_arr[x][0], help_arr[x][2], help_arr[x][1], str(datetime.timedelta(seconds=help_arr[x][3])))


