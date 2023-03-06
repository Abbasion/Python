def test(n):
    return n % 34 == 4 and n > 4 ** 4

n = 922
print(test(n))

n = 914
print(test(n))

n = 854
print(test(n))