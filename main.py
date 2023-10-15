import pandas as pd
import numpy as np

data = pd.read_csv('Employee.csv')
data.head()

data.shape

data.describe()

data.describe()
print('')

if data.isnull().any().any():
    data = data.fillna(0)
print('')

col_dic = {
    'Education': 'educacao',
    'JoiningYear': 'ano_adesao',
    'City': 'cidade',
    'PaymentTier': 'nivel_pagamento',
    'Age': 'idade',
    'Gender': 'genero',
    'EverBenched': 'trabalho_atribuido',
    'ExperienceInCurrentDomain': 'experiencia_area_atual',
    'LeaveOrNot': 'sair_ou_nao'

}
print('')

data = data.rename(col_dic, axis=1)
data.head()
print('')

# Verificando se há algum valor NaN no DataFrame
tem_nan = data.isnull().any().any()

if tem_nan:
    print("Seu DataFrame tem valores NaN.")
else:
    print("Seu DataFrame não tem valores NaN.")

data.genero.value_counts()

data.educacao.value_counts()
print('')

#apagando a ultima coluna do data-frame
#data = data.drop(columns="sair_ou_nao", inplace=True)
data = data.drop(data.columns[-1], axis=1)
data.shape
print('')

# Printando o nome dos funciinarios com a maior idade
funcionario_mais_velho = data[data['idade'] == data['idade'].max()]
print(funcionario_mais_velho)
print('')

# Filtrar funcionários com PHD, nivel de pagamento igual a 1 e experiencia_na_area_atual maior que 1
df_filtrado = data[(data['educacao'] == 'PHD') & (data['nivel_pagamento'] == 1) & (data['experiencia_area_atual'] > 1)]
print('')

# Ordenandp por idade dos mais novos
df_filtrado = df_filtrado.sort_values(by='idade', ascending=True)
print(df_filtrado)
print(df_filtrado.shape)
print('')

# Definindo uma função para calcular a média
def media(x):
    return x.mean()

# Agrupando por "genero" e medindo a media salarial por genero
media_genero = funcionario_mais_velho.groupby('genero')['nivel_pagamento'].apply(media)

print(media_genero)
print('')

df_ordenado = data.sort_values(by='experiencia_area_atual', ascending=False)

# Imprimir as pessoas ordenadas pela experiência
print(df_ordenado)
print('')

# Cria uma nova coluna chamada 'idade_inicial'
data['idade_inicial'] = data['idade'] - data['experiencia_area_atual']
print(data)
print('')

#Contar a quantidade de cidades
contagem_cidades = data['cidade'].value_counts()
print('')

# Somar a quantidade de genero
soma_genero = data['genero'].value_counts()
print('')

# Dividir a soma do genero pela quantidade total de cada cidade
resultado = soma_genero / contagem_cidades
print(resultado)
print('')

# Contagem do número total de cidades
total_cidades = data['cidade'].nunique()

# Contagem do número de gêneros por cidade
genero_por_cidade = data.groupby(['cidade', 'genero']).size().unstack(fill_value=0)

# Cálculo do percentual de gêneros por cidade
percentual_genero_por_cidade = genero_por_cidade.div(genero_por_cidade.sum(axis=1), axis=0) * 100

print(f'Total de cidades: {total_cidades}')
print('')

# Exibindo o percentual de gêneros por cidade linha a linha com um laço for
for cidade in percentual_genero_por_cidade.index:
    print(f'\nCidade: {cidade}')
    print((percentual_genero_por_cidade.loc[cidade]).apply(lambda x: '{:.2f}%'.format(x)))
print('')

#utilizando filtros, query ou where
filtro1 = data.query('ano_adesao == 2017 and experiencia_area_atual > 1').head(10)
print(filtro1)
print('')

data[data['cidade'].str.contains('Delhi')].head(10)
print('')

data.query("educacao == 'PHD' and cidade == 'New Delhi'").head()
print('')

pd.cut(data['idade'], bins=[18,29,44,60,74,90], labels=['jovem adulto', 'adulto', 'meia idade', 'idoso', 'ancião'])
print('')

data.to_csv('novo_dataframe.csv', index=False)

data.groupby('cidade')['educacao'].value_counts().plot(kind='barh')
print('')

percentual_genero_por_cidade.plot(kind='barh')

data.groupby('educacao')['genero'].value_counts().plot(kind='barh')

# plotando um grafico de faixa etaria usando o pd.cut
data['faixa_etaria'] = pd.cut(data['idade'], bins=[18,26,40,60,74,90], labels=['jovem adulto', 'adulto', 'meia idade', 'idoso', 'ancião'])
data['faixa_etaria'].value_counts().plot(kind='barh')