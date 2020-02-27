L = [5, 10, 15, 20, 25]  # Cria uma lista
for z in enumerate(L):  # o comando enumerate pega o indice e o número na posição indice
    # z neste caso é umatupla (Indice, Numero)
    x, e = z  # Separa z em duas variaveis
    print("[%d] %d" % (x, e))  # Imprime o indice e o valor usando as duas variaveis
    print(z)    # Imprime o indice e o valor como tupla
    print("="*10)  # Imprime a "separação"
