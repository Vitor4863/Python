nome = "Joao"
idade = 22
altura = 1.75
apredendo_python = True


print("Nome: ", nome)
print("Idade:" , idade)
print("Altura:" , altura)
print("Esta aprendendo Python" , apredendo_python)



#Operações Matematicas 

nota1 = 8.5
nota2 = 7.0
media = (nota1 + nota2) / 2 


print("Media do aluno ", media)

if media >= 7:
    print("Aluno aprovado")

else :
    print("Aluno reprovado")





alunos = {"João" : 5 , "Camila": 6, "jose": 8 , "Maria" : 2, "Rafael": 10}


for nome , nota in alunos.items():
    print(nome , "tirou" , nota)


media = sum(alunos.values()) / len(alunos)

maximo = max(alunos.values())

minima = min(alunos.values())

melhor_aluno = max(alunos, key = alunos.get)
pior_aluno = min(alunos , key = alunos.get )

print("Melhor aluno ", melhor_aluno)
print ("pior_aluno", pior_aluno )
print("Minimo" , minima)

print("Nota Maxima " , maximo) 

print("Media da turma " , media)
for nome , nota  in alunos.items():
    if nota >= 5:
        print(f"{nome} foi aprovado  nota{nota}")

    else:
        print(f"{nome} foi reprovado nota {nota}")






