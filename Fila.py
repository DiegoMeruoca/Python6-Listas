ultimo=5
fila=list(range(1,ultimo+1))
while True:
    print("\nExistem %d clientes na fila" %len(fila))
    print("Fila atual:",fila)
    print("Digite F para adicionar um cliente na fila,")
    print("ou A para realisar o atendimento. S para sair.")
    operacao=input("Operação (F, A ou S):")
    if operacao=="A" or operacao=="a":
        if len(fila)>0:
            atendido=fila.pop(0) # o 0 pega o primeiro da lista que representa o primeiro da fila
            print("\n>>>Cliente %d atendido<<<"%atendido)
        else:
            print("\n>>>Fila vazia ninguém para atender.<<<")
    elif operacao=="F" or operacao=="f":
        ultimo+=1 #incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao=="S" or operacao=="s":
        break
    else:
        print("Operação Inválida! Digite apenas F, A ou S")
