def despertador(dia, folga):
    # Verifica se é um dia de folga
    if folga:
        # Se for um dia de folga (sábado ou domingo), retorna 'off'
        if dia == 0 or dia == 6:
            return 'off'
        # Se for um dia de folga que não é sábado nem domingo, retorna '10:00'
        else:
            return '10:00'
    else:
        # Se não for um dia de folga (dias úteis de segunda a sexta), retorna '07:00'
        if dia >= 1 and dia <= 5:
            return '07:00'
        # Se não for um dia de folga e não for um dia útil, retorna '10:00'
        else:
            return '10:00'


# Exemplos de chamada da função
print(despertador(1, False))  # Deve retornar '07:00'
print(despertador(0, True))   # Deve retornar 'off'
print(despertador(5, True))   # Deve retornar '10:00'
