def z_function_trivial(s):
    n = len(s)
    z = [0]*n
    i = 1
    while i < n:
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:        # Пока мы не дошли до конца и символ на позиции z[i] равен
            # символу на рассматриваемой позиции+z[i]
            # (т.е., это и есть основная проверка)
            z[i] += 1
        i += 1
    return z

print(*z_function_trivial(input()))
