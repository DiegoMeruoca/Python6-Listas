L = [5, 10, 15, 20, 25]   # Cria uma lista
p = int(input("Digite o valor procurado:"))  # Entrada de dados
for e in L:  # Para cada elemento na lista
    if e == p:  # Se o elemento atual for igual p(valor pesquisado)
        print("%d faz parte da lista." % p)  # Saída de dados
        break  # Quebra o laço do for
else:  # Se o brak n for executado
    print("%d não encontrado." % p)  # Saída de dados
