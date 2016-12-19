try:
    print('Я живой!')
    raise NameError
except NameError:
    try:
        print('Ой, откуда здесь NameError?')
        raise IndexError
    except IndexError:
        print('Елы палы, а Index Error откуда мог вылезти?')