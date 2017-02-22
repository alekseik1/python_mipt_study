def reverse(A):
    for i in range(len(A)):
        A[i] = A[-1-i]
B = [1, 2, 3, 4, 5]
reverse(B)
print(B)
