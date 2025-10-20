import pandas as pd


df  = pd.read_csv("Vendas.csv")
print("Dados originais ")
print(df)


df['Quantidade']  = df["Quantidade"].fillna(0)
df['Preco'] = df["Preco"].fillna(0)

df['Total'] = df["Quantidade"] * df["Preco"] 

df = df.rename(columns={'Produto':'produto','Quantidade':'quantidade','Preco':'preco' , 'Data':'data'})


df['data'] = pd.to_datetime(df['data'])


df = df[df['Total']>0]


df.to_csv("vendas_tratadas.csv", index=False)
df.to_excel("vendas_tratadas.xlsx", index=False)
print("\nDados tratados:")
print(df)