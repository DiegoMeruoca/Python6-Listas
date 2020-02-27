L = []  # Cria uma lista vazia
print(L)  # Imprime a lista
print(len(L))  # Imprime a quantidade de itens na lista
L.append("a")  # Adiciona "a" na lista
L.append("b")  # Adiciona "b" na lista
print(L)  # Imprime a lista
print(len(L))  # Imprime a quantidade de itens na lista
L.append(["c", "d", "e"])  # Adiciona uma lista na lista na lista
print(L)  # Imprime a lista
print(len(L))  # Imprime a quantidade de itens na lista
L.extend(["f", "g", "h"])  # Adiciona os itens da lista na outra
print(L)  # Imprime a lista
print(len(L))  # Imprime a quantidade de itens na lista
del L[2]  # Deleta o item na posição 2 da lista
print(L)  # Imprime a lista
print(len(L))  # Imprime a quantidade de itens na lista
