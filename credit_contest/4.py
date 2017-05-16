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
        try:
            res.update({b: res[b] + [a]})
        except KeyError:
            res.update({b: [a]})
    # Пафосный вывод вида {вершина: кратность}
    return [{i: len(res[i])} for i in res]
print(vopros_4())
