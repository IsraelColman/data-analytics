# Israel Colman
# 11/18/2026
# Using Lambdas and generators


doubler = lambda n: n * 2

print(doubler('banana'))


tripler = lambda n: n * 3

print(tripler('banana'))


def multiplier(num):
    return lambda n: n * num

times4 = multiplier(4)
times5 = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 = multiplier(9)
times10 = multiplier(10)

print(times4(2))
print(times5(2))
print(times6(2))
print(times7(2))
print(times8(2))
print(times9(2))
print(times10(2))