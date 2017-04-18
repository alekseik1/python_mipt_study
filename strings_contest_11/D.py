def magic(s, ex):
    i = 0
    for i in range(len(s)):
        if s == ex:
            return i
        i += 1
        s = s[1:] + s[0]
    return -1

a = input()
b = input()
print(magic(a, b))
