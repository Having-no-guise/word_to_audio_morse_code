import winsound
import time
import random

code = {'А': '.-',
        'Б': '-...',
        'В': '.--',
        'Г': '--.',
        'Д': '-..',
        'Е': '.',
        'Ж': '...-',
        'З': '--..',
        'И': '..',
        'Й': '.---',
        'К': '-.-',
        'Л': '.-..',
        'М': '--',
        'Н': '-.',
        'О': '---',
        'П': '.--.',
        'Р': '.-.',
        'С': '...',
        'Т': '-',
        'У': '..-',
        'Ф': '..-.',
        'Х': '....',
        'Ц': '-.-.',
        'Ч': '---.',
        'Ш': '----',
        'Щ': '--.-',
        'Ъ': '.--.-.',
        'Ы': '-.--',
        'Ь': '-..-',
        'Э': '...-...',
        'Ю': '..--',
        'Я': '.-.-',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'}  # словарь символов

'''
за единицу времени принимается длительность короткого сигнала (одной точки);
длительность тире равно длительности трём точкам;
пауза между элементами одного знака — одна точка;
пауза между знаками в слове — три точки;
пауза между словами — семь точек.
'''


def output(mass, frequency, point, dash, sleep_spase):
    for group in mass:
        for i in group:
            if i == ' ':
                time.sleep(sleep_spase)
            if i in code.keys() and i != ' ':
                symbol = code[i]
                for j in symbol:
                    if j == '.':
                        winsound.Beep(frequency, point)
                        time.sleep(point / 1000)
                    if j == '-':
                        winsound.Beep(frequency, dash)
                        time.sleep(point / 1000)
            time.sleep(point * 3 / 1000)
        time.sleep(sleep_spase)


def main():
    print('Данная программа является аналогом АДКМ. На вход подается частота звука, скорость "точки", количество групп'
          ' и символов в группе, а также сами символы (русский алфавит и цифры)')
    while True:
        try:
            frequency = int(
                input('Введите частоту воспроизводимого сигнала (в Гц): '))  # Частота воспроизводимого звука
            point = int(
                input('Введите длительность "точки" (влияет на скорость воспроизведения): '))  # длительность "точки"
            count_of_group = int(input('Введите количество групп: '))
            count_of_symbol = int(input('Введите количество символов в группе: '))
            break
        except ValueError:
            print('Было введено не число')
    dash = point * 3
    sleep_spase = point * 7 / 1000  # time.sleep(time) time in second
    flag = True
    while flag:
        line = input('Введите символы (русская раскладка, заглавные буквы) ')
        for i in line:
            if i not in code.keys():
                print('Некоторые символы не были найдены в таблице, попробуйте еще раз')
                break
            else:
                flag = False
    mass = []
    for j in range(count_of_group):
        group = ''
        for x in range(count_of_symbol):
            group += line[random.randint(0, len(line)-1)]
        mass.append(group)

    output(mass, frequency, point, dash, sleep_spase)


if __name__ == '__main__':
    main()
