L = [1, 7, 2, 4]  # Cria a Lista
minimo = L[0]  # Adiciona o item na posição 0 na variavel minimo
for e in L:  # para cada elemento na lista L
    if e < minimo:  # se o elemento for menor que a variavel minimo
        minimo = e  # variavel minimo recebe o elemento
print(minimo)  # imprime a variavel minimo
