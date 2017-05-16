# Сортировка выбором.
# O(n^2)
def select_sort(l):
    for k in range(len(l) - 1):
        m = k
        i = k + 1
        while i < len(l):
            if l[i] < l[m]:
                m = i
            i += 1
        t = l[k]
        l[k] = l[m]
        l[m] = t

# TODO: добавить тесты
