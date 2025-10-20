import pandas as pd
import requests
from io import StringIO

# ======================
# 1️⃣ EXTRACT - Puxar dados da web
# ======================
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
response = requests.get(url)

# Ler CSV direto do conteúdo da web
data = StringIO(response.text)
df = pd.read_csv(data)

print("Dados originais:")
print(df[['location','date','total_cases','total_deaths']].head())

# ======================
# 2️⃣ TRANSFORM - Limpeza e transformação
# ======================

# Selecionar colunas importantes
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

# Preencher valores faltantes com 0
df[['total_cases', 'new_cases', 'total_deaths', 'new_deaths']] = df[['total_cases', 'new_cases', 'total_deaths', 'new_deaths']].fillna(0)

# Converter coluna 'date' para datetime
df['date'] = pd.to_datetime(df['date'])

# Filtrar apenas dados do Brasil
df_brasil = df[df['location'] == 'Brazil'].copy()

# Filtrar datas mais recentes (exemplo: últimos 3 anos)
df_brasil = df_brasil[df_brasil['date'] >= '2022-01-01']

# Criar coluna de casos ativos
df_brasil['active_cases'] = df_brasil['total_cases'] - df_brasil['total_deaths']

# Ordenar por data
df_brasil = df_brasil.sort_values(by='date')

# ======================
# 3️⃣ LOAD - Salvar relatório final
# ======================
df_brasil.to_csv("covid_brasil_tratado.csv", index=False)
df_brasil.to_excel("covid_brasil_tratado.xlsx", index=False)

print("\nDados tratados (Brasil):")
print(df_brasil.head())
print("\nArquivo salvo com sucesso!")
