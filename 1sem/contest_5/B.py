def Capitalize(S):
    S = S.split()
    b = []
    for i in S:
        k = i[0].upper() + i[1:].lower()
        b.append(k)
    return b
print(*Capitalize(input()))