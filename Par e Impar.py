V = [9, 8, 7, 12, 0, 13, 21, 44]  # Cria a Lista
P = []  # Cria uma lista vazia para os pares
I = []  # Cria uma lista vazia para os Impares
for e in V:  # Para cada elemnto na lista V
    if e % 2 == 0:  # Se o resto da divisão de elemento por 2 é 0
        P.append(e)  # Adiciona o elemto na lista P
    else:  # Senão
        I.append(e)   # Adiciona o elemto na lista I
print("Pares: ", P)  # Imprime a lista P - pares
print("Impares: ", I)  # Imprime a lista I - impares
