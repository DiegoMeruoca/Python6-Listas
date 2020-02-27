compras = []  # Cria a lista compra vazia
print("Digite a lista de compras, digite fim para sair.")  # Mensagem
while True:  # Enquanto verdadeiro (Loop infinito)
    produto = input("Produto:")  # Lê o produto digitado
    if produto.upper() == "FIM":  # Se for digitado fim
        break  # Encerra o loop infinito
    compras.append(produto)  # Adiciona o produto digitado na lista
print("="*90)
print("Lista de compras:")  # Mensagem
for p in compras:  # Para cada produto na lista compras
    print(p)  # Imprime o produto
print("="*90)
