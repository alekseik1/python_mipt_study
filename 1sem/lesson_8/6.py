dict = dict()
sl = open('en-ru_6.txt')
slt = open('output.txt', 'w')
s = sl.readline().rstrip()
while len(s) > 0:
    en_trans, ru_trans = list(s.split('\t-\t'))
    if ',' in ru_trans:
        for i in ru_trans.split(','):
            i = i.lstrip()
            if i in dict:
                dict[i] = dict[i]+', '+en_trans
            else:
                dict[i] = en_trans
    else:
        if ru_trans in dict:
            dict[ru_trans] = dict[ru_trans]+', '+en_trans
        else:
            dict[ru_trans] = en_trans

    s = sl.readline().rstrip()

key_sort = sorted(dict.keys())
for i in key_sort:
    print('\t-\t'.join((i, dict[i])), file=slt)
