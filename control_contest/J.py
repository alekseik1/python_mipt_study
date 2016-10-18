def Capitalize(s):
    s = s.upper()
    l = ''
    for i in range(len(s)-1,0,-1):
        if (90>=ord(s[i])) and (ord(s[i])>=65) and (90>=ord(s[i-1])) and (ord(s[i-1])>=65):
            l = s[i].lower() + l
        else:
            l = s[i] + l
    l = s[0] + l
    return l
str = input()
str = Capitalize(str)
print(str)