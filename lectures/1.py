def z_finction_trivial(s):
    n = len(s)
    z = [0]*n
    i = 1
    while i < n:
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        i += 1
    return z

print(z_finction_trivial('abacaba'))
