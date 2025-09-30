import pandas as pd

# Criando um DataFrame (tabela) com dados fictícios
dados = {
    "Aluno": ["joão" , "Maria" , "Rafael" , "Camila" , "Jose"],
    "Nota": [7.5, 9.0,6.0,8.5,5.0],
    "Idade":[20,22, 21, 19, 23]
}

df = pd.DataFrame(dados)
# Mostrar a tabela
print("Tabela de Dados")
print(df)


# Estatísticas básicas

print("/n Estatitisticas")
print(df.describe)


#Media das notas

media = df["Nota"].mean()
print(f"\nMédia das notas: {media:.2f}")

aprovados = df[df["Nota"] >= 7]
print("\n Alunos Aprovados : ")
print(aprovados)