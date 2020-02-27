L = ["Azul", "Verde", "Vermelho", "Preto", "Branco"]   # Cria uma lista
p = input("Digite o valor procurado:").capitalize()  # Entrada de dados
achou = False  # Defina a variavel achou para Falso
x = 0  # Define x como 0
while x < len(L):  # Enquanto x for menor que o comprimento da Lista
    if L[x].capitalize() == p:  # Se o numero na posição x for igual ao valor procurado
        achou = True  # Acchou recebe Verdadeiro
        break  # Quebra o laço
    x += 1  # x rebe o valor atual mais 1
if achou:  # se achou
    print("%s achado na posição %d." % (p, x))  # Saída de dados
else:  # se não achou
    print("%s não encontrado." % p)  # Saída de dados
