from sys import setrecursionlimit


def F(n):
    if n <= 1:
        return 1
    else:
        return F(n - 2) * 2
        # if n % 2 == 0:
        #     return F(n - 1)/3
        # else:
        #     return F(n - 1) * 6


setrecursionlimit(5000)
print(F(2049) / F(2046))