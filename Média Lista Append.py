import sys
print("Bem vindo ao progranma de calculo de médias!!!\n")
notas=[]
soma=0.0
nome=input("Digite o nome do(a) aluno(a):")
x=0
while True:
    dig=input("Digite a nota %d do aluno ou S para sair:" %(x+1))
    if dig=="S" or dig=="s":
        break
    nota=float(dig)
    notas.append(nota)
    soma=soma+notas[x]
    x=x+1
if len(notas)==0:
    print("Voce não digitou nenhuma nota, portando não há dados suficientes para calculo da média.")
    sys.exit()
x=0    
while x<len(notas):
    print("Nota %d = %5.2f"%(x+1,notas[x]))
    x=x+1
media=soma/x
if media>=7:
    status="aprovado(a)"
else:
    status="reprovado(a)"
print("A média do(a) %s foi %5.2f. Portatdo está %s!!!" %(nome,media,status))
                   
