import string
f = open('../LICENSE')
a = {}
mytext = "test text for testing only text"
s = f.read().split()
for i in range(len(s)):
    s[i] = s[i].lower()
for i in range(len(s)):
    k = ''
    for j in s[i]:
        if j not in string.punctuation:
            k += j
        else:
            k += ' '
    s[i] = k
k = ''
for i in s:
    k += i + ' '
k = k.split()
s = k
print(k)
for i in s:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
for i in a:
    print(i, ':', a[i])
maxi = 1
maxi_word = ''
for i in a:
    if a[i] > maxi:
        maxi = a[i]
        maxi_word = i
print('Max: ', maxi_word, '-', maxi)
