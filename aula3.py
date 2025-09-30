import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


dados =  {
  "Aluno": ["João", "Maria", "Rafael", "Camila", "José"],
    "Nota": [7.5, 9.0, 6.0, 8.5, 5.0],
    "Idade": [20, 22, 21, 19, 23]
}



df = pd.DataFrame(dados)


plt.figure(figsize=(8,5))
sns.barplot(x="Aluno", y="Nota", data=df, palette="viridis")
plt.title("Notas dos alunos")
plt.ylabel("Nota")
plt.xlabel("Aluno")
plt.show()


plt.figure(figsize=(8,5))
sns.histplot(df["Nota"] , bins = 5, kde=True , color="blue")
plt.title("Distribuição das Notas ")
plt.xlabel("Nota")
plt.ylabel("Quantidade de alunos")
plt.show()