f = open('en-ru_6.txt')
s = f.read().split('\n')
dic = {}
for i in range(len(s)):
    tmp = s[i].split('\t-\t')
    dic[tmp[0]] = tmp[1]
dic = {dic[a]: a for a in dic}
print(dic)
#l = dic.keys()
#l = list(l)
#l.sort()
#print(l)
#print(l)
#l.sort()
#for i in l:
#    print(i, '-', dic[i], end='; ')