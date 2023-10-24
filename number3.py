var = [1, 2, 3]
varA = [2, 3]


def iguais():
    return var[0] == varA[0] or var[-1] == varA[-1]


print(iguais())
