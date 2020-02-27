print("Bem vindo ao progranma de calculo de médias!!!\n")
notas=[0,0,0,0,0]
soma=0.0
nome=input("Digite o nome do(a) aluno(a):")
x=0
while x<5:
    notas[x]=float(input("Digite a nota %d do aluno:" %(x+1)))
    soma=soma+notas[x]
    x=x+1
x=0    
while x<5:
    print("Nota %d = %5.2f"%(x+1,notas[x]))
    x=x+1
media=soma/x
if media>=7:
    status="aprovado(a)"
else:
    status="reprovado(a)"
print("A média do(a) %s foi %5.2f. Portatdo está %s!!!" %(nome,media,status))
                   
