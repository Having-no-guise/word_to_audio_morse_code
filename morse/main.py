import winsound
import time

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
        '0': '-----'}#словарь символов

'''
за единицу времени принимается длительность короткого сигнала (одной точки);
длительность тире равно длительности трём точкам;
пауза между элементами одного знака — одна точка;
пауза между знаками в слове — три точки;
пауза между словами — семь точек.
'''

def output(line, frequency, point, dash, sleep_spase):
    for i in line:
        if i == ' ':
            time.sleep(sleep_spase)
        if i in code.keys() and i != ' ':
            symbol = code[i]
            for i in symbol:
                if i == '.':
                    winsound.Beep(frequency, point)
                    time.sleep(point / 1000)
                if i == '-':
                    winsound.Beep(frequency, dash)
                    time.sleep(point / 1000)
        time.sleep(point*3/1000)


def main():
    print('Данная программа преобразует написанные буквы русского алфавит в код морзе, с максимальной скоростью около'
          ' 20 символов в минуту')
    while True:
        try:
            frequency = int(input('Введите частоту воспроизводимого сигнала (в Гц): '))  # Частота воспроизводимого звука
            break
        except ValueError:
            print('Было введено не число')
    while True:
        try:
            point = int(input('Введите длительность "точки" (минимальная длительность - 150): '))  # длительность "точки"
            break
        except ValueError:
            print('Было введено не число')
    dash = point*3
    sleep_spase = point*7/1000 #time.sleep(time) time in second
    flag = True
    while flag:
        line = input('Введите символы (русская раскладка, заглавные буквы) ')
        for i in line:
            if i not in code.keys():
                print('Некоторые символы не были найдены в таблице, попробуйте еще раз')
                break
            else:
                flag = False
    output(line, frequency, point, dash, sleep_spase)


if __name__ == '__main__':
    main()

