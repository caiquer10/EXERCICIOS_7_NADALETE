var = [1, 2]


def soma(num):
    # Verifica se a lista tem pelo menos dois elementos
    if len(num) >= 2:
        # Retorna a soma dos dois primeiros elementos da lista
        return num[0] + num[1]
    # Verifica se a lista tem exatamente um elemento
    elif len(num) == 1:
        # Retorna o único elemento da lista (neste caso, num[0])
        return num[0]
    else:
        # Retorna 0 caso a lista esteja vazia
        return 0


print(soma(var))
