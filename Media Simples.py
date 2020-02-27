notas = []  # Cria a lista notas vazia
print("Digite as notas do aluno, digite fim para sair.")  # Mensagem
while True:  # Enquanto verdadeiro (Loop infinito)
    nota = input("Nota:")  # Lê a nota digitada
    if nota.upper() == "FIM":  # Se for digitado fim
        break  # Encerra o loop infinito
    notas.append(float(nota))  # Adiciona a nota digitada na lista
total = 0.0
cont = 0
for n in notas:  # Para cada nota na lista notas
    total += n  # soma a nota aos outros valores na variavel total
    cont += 1  # adiciona mais um no contador
media = total / cont
print("="*90)
print("A média do aluno foi %5.2f!" % media)
print("="*90)
