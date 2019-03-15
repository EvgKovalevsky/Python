"""ohlc_script with CLI"""
from csv import reader, writer
from datetime import datetime, timedelta
from os.path import exists, join
from os import makedirs
import argparse


def opencsv(path):
    """Open .csv input"""
    _data = []
    with open(path, "r") as file:
        csvreader = reader(file)
        for row in csvreader:
            temp = row[3].split()
            _data.append([row[0], row[1], row[2], temp[0], temp[1]])
    return _data


def createcsv(path, filename, data):
    """Write data in .csv output"""
    filepath = join(path, filename)
    if not exists(path):
        makedirs(path)
    with open(filepath, "w") as file:
        csvwriter = writer(file)
        for row in data:
            csvwriter.writerow(row)


def ohlc(data, interval):
    """Create candles from raw data"""
    date = [int(i) for i in data[0][3].split('-')]
    dstart = datetime(date[0], date[1], date[2], 7)
    dend = dstart + timedelta(seconds=interval * 60)
    _data, temp = [], []
    for line in data:
        date = [int(i) for i in line[3].split('-')]
        time = [int(i) for i in line[4][0:5].split(':')]
        dnow = datetime(date[0], date[1], date[2], time[0], time[1])
        if dnow.hour not in range(3, 7):
            if dnow >= dend:
                if dend.hour == 3:
                    dstart += timedelta(seconds=240 * 60)
                else:
                    dstart = dend
                dend = dstart + timedelta(seconds=interval * 60)
                _data += temp
                temp.clear()
            for elem in temp:
                if elem[0] == line[0]:
                    temp[temp.index(elem)][3:] = [max(elem[3], line[1]),
                                                  min(elem[4], line[1]),
                                                  line[1]]
                    break
            else:
                value = [line[0], dstart.strftime('%Y-%m-%dT%H:%M:00Z'),
                         line[1], line[1], line[1], line[1]]
                temp.append(value)
    _data += temp
    return _data


PARSER = argparse.ArgumentParser(prog='OHLC_script',
                                 description='Программа строит OHLC графики.',
                                 prefix_chars='--')
PARSER.add_argument('--full_info', action='store_true', default=False,
                    help='Краткое описание всех функции в программе.')
PARSER.add_argument('--file', default='trades.csv', type=str,
                    help='Указывает исходный .csv файл.')
PARSER.add_argument('--output', default='Output', type=str,
                    help='Указывает выходную директорию.')
ARGS = PARSER.parse_args()
if ARGS.full_info:
    print('1) opencsv(path) - открытие исходного .csv файла.\n' +
          '\tpath - путь к файлу.')
    print('2) createcsv(path, filename, data) - создание выходного .csv ' +
          'файла.\n' +
          '\tpath - директория к файлу;\n' +
          '\tfilename - имя файла;\n' +
          '\tdata - выходные данные.')
    print('3) ohlc(data, interval) - создание свечного графика ' +
          'с определенным интервалом.\n' +
          '\tdata - исходные данные;\n' +
          '\tinterval - интервал графика.')
elif exists(ARGS.file):
    INPUT_DATA = opencsv(ARGS.file)
    createcsv(ARGS.output, 'ohlc_5min.csv', ohlc(INPUT_DATA, 5))
    createcsv(ARGS.output, 'ohlc_30min.csv', ohlc(INPUT_DATA, 30))
    createcsv(ARGS.output, 'ohlc_240min.csv', ohlc(INPUT_DATA, 240))
else:
    print('File not exist!')
