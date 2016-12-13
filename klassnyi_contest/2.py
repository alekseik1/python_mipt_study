import os
import sys
def A():
    A = os.environ
    B = sys.argv
    if len(B) == 1:
        return
    k = 1
    max_k = int(B[1])
    for i in B[2:]:
        if k > max_k:
            return
        try:
            print(i + '=' + A[i])
            k += 1
        except:
            pass
A()