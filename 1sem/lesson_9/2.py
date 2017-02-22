import argparse
parser = argparse.ArgumentParser(
    # краткое описание программы
    description='IT-калькулятор'
)

# описываем позиционные параметры
parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем что ожидаются числа с плавающей запятой
    type=float,
    # параметров будет не меньше одного
    nargs='+',
    # краткое описание параметров
    help='два числа'
)

parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='Быть чуточку общительнее'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-a',
    # длинное название опции
    '--action',
    # парсер сохранит значение True, если встретит эту опцию
    metavar='ACTION',
    # краткое описание опции
    help='Арифм. действие'
)

# вызываем функцию разбора параметров командной строки
args = parser.parse_args()
val = [x for x in args.values]
act = args.action
if act != '+' and act != '-' and act != '/' and act != '*':
    print('unknown operator')
    exit(-1)
else:
    if not args.verbose:
        print(eval(str(val[0])+act+str(val[1])))
    else:
        print(str(val[0]) +' ' + act+ ' '+str(val[1]) + ' = ' + str(eval(str(val[0])+act+str(val[1]))))