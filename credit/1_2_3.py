def vopros_1_orientated():
    '''
     От списка ребер к матрице смежности, ориентированный вариант. 
    :return: 
    '''
    res = {}
    while True:
        s = input()
        if s == "":
            break
        a, b = map(int, s.split())
        try:
            res.update({a: res[a] + [b]})
        except KeyError:
            res.update({a: [b]})
    return res

def vopros_1_nonorientated():
    '''
     От списка ребер к матрице смежности, неориентированный вариант. 
    :return: 
    '''
    res = {}
    while True:
        s = input()
        if s == "":
            break
        a, b = map(int, s.split())
        try:
            res.update({a: res[a] + [b]})
        except KeyError:
            res.update({a: [b]})
        try:
            res.update({b: res[b] + [a]})
        except KeyError:
            res.update({b: [a]})
    return res

def vopros_2():
    '''
    От списка рёбер взвешенного ориентированного графа к спискам смежности.
    :return: 
    '''
    res = {}
    while True:
        s = input()
        if s == "": break
        a, b = map(int, s.split())
        try:
            res[a] = res[a].append(b)
        except KeyError:
            # Если у нас еще ни разу не вводили этот элемент
            res.update({a: b})
    return res

# Простите, я просто скопировал вопрос 2
def vopros_3():
    '''
    От списка рёбер невзвешенного неориентированного графа к спискам смежности. 
    :return: 
    '''
    res = {}
    while True:
        s = input()
        if s == "": break
        a, b = map(int, s.split())
        try:
            res[a] = res[a].append(b)
        except KeyError:
            # Если у нас еще ни разу не вводили этот элемент
            res.update({a: b})
    return res


print(vopros_1_nonorientated())
