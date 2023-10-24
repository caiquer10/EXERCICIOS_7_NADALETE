def maior_ponta(nums):
    if len(nums) >= 1:
        # Função maxima encontrando o maior valor entre os selecionados
        maior = max(nums[0], nums[-1])
        return [maior] * len(nums)
    else:
        return []


lista1 = [1, 2, 3]
lista2 = [4, 2, 3]
var2 = []

print(maior_ponta(lista1))
print(maior_ponta(lista2))
print(maior_ponta(var2))
