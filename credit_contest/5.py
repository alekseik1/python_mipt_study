def vopros_4():
    '''
    Матрицей смежности задан неориентированный граф. Выведите степень каждой вершины.
    :return: 
    '''
    res = {}
    while True:
        s = input()
        if s == "": break
        a, b = map(int, s.split())
        try:
            res.update({a: res[a] + [b]})
        except KeyError:
            res.update({a: [b]})
    # Пафосный вывод вида {вершина: кратность}
    s = [{i: 0} for i in res]
    for i in res:
        for j in res[i]:
            if i == j:
                s[i] = s[i] + 1

    return [{i: len(res[i])} for i in res]
print(vopros_4())