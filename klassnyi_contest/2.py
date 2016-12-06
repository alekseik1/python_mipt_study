import os
import sys
A = os.environ
B = sys.argv
for i in B[1:]:
    try:
        print(i + '=' + A[i])
    except:
        pass