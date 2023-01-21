# Collins Wanga


def accumulator(n):
    sum = 0
    for k in range(1,n):
        sum = sum + (1/(k**2))
    return sum
