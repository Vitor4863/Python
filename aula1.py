import csv

alunos = {"João" : 5 , "Camila": 6, "jose": 8 , "Maria" : 2, "Rafael": 10}


relatorio = []

for nome , nota in alunos.items():
    situacao = "Aprovado" if nota >= 7 else "Reprovado"
    relatorio.append({"Nome": nome, "Nota": nota, "Situação": situacao})


    media = sum(alunos.values()) / len(alunos)
    melhor_aluno = max(alunos , key = alunos.get)
    pior_aluno = min(alunos , key = alunos.get)


  



with open("relatorio_turma.csv", "w", newline="") as arquivo:
    campos = ["Nome", "Nota", "Situação"]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(relatorio)


 
print("Relatório salvo com sucesso em 'relatorio_turma.csv'!")

# Mostrar estatísticas no terminal
print(f"Média da turma: {media:.2f}")
print(f"Melhor aluno: {melhor_aluno} ({alunos[melhor_aluno]})")
print(f"Pior aluno: {pior_aluno} ({alunos[pior_aluno]})")