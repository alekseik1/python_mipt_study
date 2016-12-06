import sys
try:
    A = sys.argv[1]
    f = open('output.txt', 'w')
    try:
        f.write(sys.getsizeof(A))
        f.close()
        exit(0)
    except:
        f.write('Can\'t open file' + ' ' + A)
        f.close()
        exit(2)
except:
    #Другая посылка
    f = open('output.txt', 'w')
    f.write('Usage: stat filename')
    f.close()
    exit(1)
