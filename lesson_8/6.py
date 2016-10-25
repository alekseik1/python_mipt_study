import string
f = open('en-ru_6.txt')
s = f.read().split('\n')
dic = {}
for i in range(len(s)):
    tmp = s[i].split('\t-\t')
    dic[tmp[0]] = tmp[1]
dic = {dic[a]: a for a in dic}
for i in dic:
    if i & string.punctuation != set():
        i =
print(dic)
