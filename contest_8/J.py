N = int(input())
Dict = {}
for i in range(N):
    st = input()
    if len(st) in Dict:
        Dict[len(st)] +=  '\n' + st[::-1] + ' ' + st
    else:
        Dict[len(st)] = st[::-1] + ' ' + st
for i in range(1, 16):
    if i in Dict:
        print(i)
        A = Dict[i].split('\n')
        A.sort()
        print('\n'.join(A))