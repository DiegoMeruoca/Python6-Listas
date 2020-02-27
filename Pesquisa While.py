L = [5, 10, 15, 20, 25]   # Cria uma lista
p = int(input("Digite o valor procurado:"))  # Entrada de dados
achou = False  # Defina a variavel achou para Falso
x = 0  # Define x como 0
while x < len(L):  # Enquanto x for menor que o comprimento da Lista
    if L[x] == p:  # Se o numero na posição x for igual ao valor procurado
        achou = True  # Acchou recebe Verdadeiro
        break  # Quebra o laço
    x += 1  # x rebe o valor atual mais 1
if achou:  # se achou
    print("%d achado na posição %d." % (p, x))  # Saída de dados
else:  # se não achou
    print("%d não encontrado." % p)  # Saída de dados
