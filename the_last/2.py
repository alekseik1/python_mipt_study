# Ввод массива
# Если способ работать без n?
#n = int(input())
a = []
while True:
    tmp = input()
    if tmp == '':
        break
    a.append(list(map(int, tmp.split())))
# Проверка пар и их вывод
l =
for i in a:
    if i[0] % 3 != 0 and i[1]%3 != 0 and i[0]%5!=0 and i[1]%5!=0 or (i[0] > 99 and i[1] < 100 and i[1]%2==0) or (i[1] > )