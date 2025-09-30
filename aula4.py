import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns






df = pd.read_csv("alunos.csv")

print("Visualizar primeiras linhas")

print(df.head)
print(df.describe)



media = df["Nota"].mean()
print(f"\nMedia Geral das notas {media:.2f}")


aprovados = df[df["Nota"] >=7]
print("\n Alunos Aprovados:")
print(aprovados)


media_turma = df.groupby("Turma") ["Nota"].mean()
print("\n media das notas por turma : ")
print(media_turma)


# ==== Visualizações ====



# Gráfico de barras das notas por aluno



plt.figure(figsize=(8,5))
sns.barplot(x = "Aluno" , y = "Nota" , data=df , palette="coolwarm")
plt.title("Notas por Aluno")
plt.show()



# Boxplot por turma
plt.figure(figsize=(6,5))
sns.boxplot(x="Turma", y="Nota", data=df, palette="Set2")
plt.title("Distribuição das notas por Turma")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Nota"], bins=5, kde=True, color="blue")
plt.title("Distribuição das Notas")
plt.xlabel("Nota")
plt.ylabel("Quantidade de Alunos")
plt.show()