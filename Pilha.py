prato = 5
pilha = list(range(1, prato+1))
while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para Desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S):")
    if operacao.upper() == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)  # o -1 seleciona o ultimo da lista que representa o prato emcima da pilha
            print("\n>>>Prato %d lavado<<<" % lavado)
        else:
            print("\n>>>Pilha vazia nada para lavar.<<<")
    elif operacao.upper() == "E":
        prato += 1  # mais um prato
        pilha.append(prato)
    elif operacao.upper() == "S":
        break
    else:
        print("Operação Inválida! Digite apenas E, D ou S")
