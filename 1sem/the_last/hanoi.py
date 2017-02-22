
def hanoi(n,i=1,k=3):
    if i+k==4:
        tmp=6-i-k
        hanoi(n,i,tmp)
        hanoi(n,tmp,k)
    else:                   #все остальное как на лекции
        if n==1:
            print(n,i,k)
        else:
            tmp=6-i-k
            hanoi(n-1,i,tmp)
            print(n,i,k)
            hanoi(n-1,tmp,k)
hanoi(int(input()))
# Без костылей! Ха-ха, Серега, тебя уделали