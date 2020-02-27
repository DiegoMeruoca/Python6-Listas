L = [1, 7, 2, 4]  # Cria a Lista
maximo = L[0]  # Adiciona o item na posição 0 na variavel maximo
for e in L:  # para cada elemento na lista L
    if e > maximo:  # se o elemento for maior que a variavel maximo
        maximo = e  # variavel maximo recebe o elemento
print(maximo)  # imprime a variavel maximo
