def f(n):
    if n == 3:
        return 1
    elif n < 3:
        return 0
    else:
        if n % 3 == 0:
            return f(n // 3) + f(n - 1)
        else:
            return f(n // 3) + f(n - (n % 3))

        
print(f(58))