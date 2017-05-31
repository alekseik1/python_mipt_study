def magick(reg, s):
    res = []
    k = len(reg)
    for i in range(len(s)-len(reg)+1):
        if s[i:i+k] == reg:
            res.append(i)
    if len(res) == 0:
        return [-1]
    return res
print(*magick(input(), input()))
