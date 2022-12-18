# Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
# Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) ,
# бесконечный цикл, функции и прочий функционал.
# Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать - вывести,
# показать, перезаписать , добавить событие в определенный день недели

import os.path

def get_info():
    info = []
    last_name = input('Укажите дату: ')
    info.append(last_name)
    first_name = input('Укажите время: ')
    info.append(first_name)
    phone_number = input('Укажите место положения: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def creating():
    file = 'schedule.txt'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Дата;Время;Место;Описание\n')

def writing_txt(info):
    file = 'schedule.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def read_txt():
    file = 'schedule.txt'
    with open(file, 'r', encoding='utf-8') as data:
        data1 = data.readlines()
    my_list = []
    for line in data1:
        temp = line.replace('\n', '')
        my_list.append(temp.split(';'))
    return my_list


def search_data(data, info):
    my_list_info = []
    for i in data:
        for j in i:
            if j == info:
                my_list_info.append(i)
    return my_list_info

def print_result(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end=' ')
        print()

if os.path.exists('schedule.txt'):
    while True:
        data = read_txt()
        command = int(input('Введите команду:\n1.Найти запланированное:\n2.Показать все планы:\n3.Добавить планы:\n4.Завершить работу\n'))
        if command == 1:
            com = int(input('1.Искать по дате\n2.Искать по описанию\n'))
            if com == 1:
                inf = input('Введите дату: \n')
                print(*data[0])
                print_result(search_data(data, inf))
            else:
                inf = input('Введите описание: \n')
                print(*data[0])
                print_result(search_data(data, inf))
        elif command == 2:
            print()
            print_result(read_txt())
            print()
        elif command == 3:
            info = get_info()
            writing_txt(info)
        elif command == 4:
            break
        else:
            print('Такой команды пока нет!!! ')
else:
    creating()


