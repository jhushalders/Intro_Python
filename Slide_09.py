import pandas as pd
#data frame no pandas é heterogeneo - colunas podem ter tipos diferentes
#illna(), dropna(), isna(), notna() # tratamento de dados faltantes

#Criando um DataFrame a partir de uma lista de tuplas
nomes = ['Ana', 'Bruno', 'Carla']
idades = [23, 35, 29]
dados = list(zip(nomes, idades)) 
print(dados)

df = pd.DataFrame(dados)
print(df)

#Criando um DataFrame a partir de um dicionário
dados = {'Nome': ['Ana', 'Bruno', 'Carla'],
'Idade': [23, 35, 29]}
df = pd.DataFrame(dados)
print(df)

df.columns = ['Nome', 'Idade'] # renomeando colunas
df.index = ['A', 'B', 'C'] # renomeando índices
#ou
dados = [('Ana', 23), ('Bruno', 35), ('Carla', 29)]
colunas = ['Nome', 'Idade']
linhas = ['A', 'B', 'C']
df = pd.DataFrame(dados, columns=colunas, index=linhas)
print(df)

#Explorando o DataFrame
print(df)
print(df.dtypes) # tipos de dados das colunas
print(df.shape) # dimensões do DataFrame
print(df.info()) # informações sobre o DataFrame
print(df.describe()) # estatísticas descritivas
print(df.head(2)) # primeiras linhas
print(df.tail(2)) # últimas linhas
print(df.sample(2)) # amostra aleatória
df.ndim # número de dimensões
df.index # índices
df.columns # nomes das colunas
df.size # número total de elementos
df.dtypes # tipos de dados das colunas
df.empty # verifica se o DataFrame está vazio
print(df.loc['A', 'Nome']) # acesso por rótulo
print(df.iloc[0, 0]) # acesso por posição
print(df['Nome']) # acesso por coluna
print(df[['Nome', 'Idade']]) # acesso por múltiplas colunas
print(df[df['Idade'] > 25]) # filtragem

#INDEXADORES - seleção de dados
print (df.T) #Transpõe o DataFrame (troca linhas por colunas)
df.loc[] # Acessa dados por rótulos (índices).
print(df.loc[['B','C']]) # Acessa a linhas com rótulos 'B' e 'C'
print(df.loc[['A','C'], ['Nome']]) # Acessa as linhas 'A' e 'C' e a coluna 'Nome'
print(df.loc['B', ['Nome', 'Idade']]) # Acessa a linha 'B' e as colunas 'Nome' e 'Idade'
print(df.loc[[True , False , True], 'Nome'])
df.iloc[]# Acessa dados por posições (índices numéricos)
print(df.iloc[[1, 2]]) # Acessa a linhas nas posições 1 e 2
print(df.iloc[-1]) # Acessa a última linha do 
print(df.iloc[[0, 2], [0]]) # Acessa as linhas nas posições 0 e 2 e a coluna na posição 0
df.at[] # Acessa um único valor por rótulo.
df.at['C', 'Nome'] # Acessa o valor na linha 'C' e coluna 'Nome'
df.iat[] # Acessa um único valor por posição
print(df.iat[2, 0]) # Acessa o valor na linha 2 e coluna 0

#Adicionando e modificando colunas
print(df)
df['Cidade'] = 'São Paulo' # Adiciona uma nova coluna 'Cidade' com valor padrão
print(df)
df['Cidade'] = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'] # Adiciona uma nova coluna 'Cidade' com valores diferentes
print(df)
df['Idade'] = df['Idade'] + 1 # Incrementa a idade em 1
print(df)
df['Idade'] = df['Idade'].replace({24: 25}) # Substitui idade 24 por 25
print(df)
pd.concat([df, pd.DataFrame({'Nome': ['Daniel'], 'Idade': [30], 'Cidade': ['Curitiba']})], ignore_index=True) # Adiciona uma nova linha
print(df)

#Concatenando dois DataFrames por linhas (axis=0
dados1 = [('Ana', 21,'F'), ('Bruno', 20,'M')]
df1 = pd.DataFrame(data = dados1, columns=['Nome', 'Idade','Sexo'])
print(df1)
dados = [ {'Nome': 'Carla', 'Idade': 22, 'Sexo': 'F'}, {'Nome': 'Daniel', 'Idade': 18, 'Sexo': 'M'} ]
df2 = pd.DataFrame(data = dados)
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)

#Adicionando e Modificando Linhas - Concatenando dois DataFrames por colunas (axis=1)
dados1 = [('Ana', 21), ('Bruno', 20)]
df1 = pd.DataFrame(data = dados1, columns=['Nome', 'Idade'])
print(df1)
dados2 = [('F'), ('M')]
df2 = pd.DataFrame(data = dados2, columns=['Sexo'])
df3 = pd.concat([df1, df2], axis=1)
print(df3)
#ou
df1['Sexo'] = df2['Sexo']
print(df1)

#Removendo linhas e Colunas de um DataFrame
df.drop(index=['B'], inplace=True) # Remove a linha com rótulo 'B' no DataFrame original
print(df)
df.drop(columns=['Cidade'], inplace=True) # Remove a coluna 'Cidade' no DataFrame original
print(df)
#inplace: se True, modifica o DataFrame original; se False (default), retorna um novo DataFrame.

#Operadores
dados1 = [('Ana', 21,'F'), ('Bruno', 20,'M'), ('Carla', 22,'F'), ('Daniel', 18,'M')]
df1 = pd.DataFrame(data = dados1, columns=['Nome', 'Idade','Sexo'])
print(df1)
df1['Idade'] += 1 # Incrementa a idade em 1
print(df1)
resultado = list(df1['Sexo'] == 'M') # Retorna uma lista booleana
print(resultado) # [False, True, False, True]
print(df1[resultado]) # Filtra o DataFrame com a lista booleana
resultado = df1['Sexo'] == 'M' # Retorna uma Series booleana
print(df1[resultado]) # Filtra o DataFrame com a Series booleana
resultado = df1['Idade'] > 20 # Retorna uma Series booleana
print(df1[resultado]) # Filtra o DataFrame com a Series booleana
resultado = (df1['Idade'] > 20) & (df1['Sexo'] == 'F') # Combina duas condições com AND
df_masculino = df1.loc[df1['Sexo'] == 'M'] # Filtra o DataFrame com a condição
print(df_masculino)

#ordenando um dataframe
df_ordenado = df1.sort_values(by='Idade') # ordena por idade crescente
print(df_ordenado)
df_ordenado_desc = df1.sort_values(by='Idade', ascending=False) # ordena por idade decrescente
print(df_ordenado_desc)
df_ordenado_multi = df1.sort_values(by=['Sexo', 'Idade']) # ordena por sexo e idade
print(df_ordenado_multi)

#métodos estáticos
df_copy = df1.copy() # cria uma cópia do DataFrame
print(df_copy)
df_unique = df1['Sexo'].unique() # retorna os valores únicos da coluna 'Sexo'
print(df_unique)
count = df1['Sexo'].value_counts() # conta os valores da coluna 'Sexo'
print(count)
mean_idade = df1['Idade'].mean() # calcula a média da coluna 'Idade'
print(mean_idade)
max_idade = df1['Idade'].max() # calcula o máximo da coluna 'Idade'
median_idade = df1['Idade'].median() # calcula a mediana da coluna 'Idade'
std_idade = df1['Idade'].std() # calcula o desvio padrão da coluna 'Idade'
var_idade = df1['Idade'].var() # calcula a variância da coluna 'Idade'
min_idade = df1['Idade'].min() # calcula o mínimo da coluna 'Idade'
sum_idade = df1['Idade'].sum() # calcula a soma da coluna 'Idade'
describe = df1.describe() # estatísticas descritivas do DataFrame
print(describe)
df1.head(2) # primeiras 2 linhas do DataFrame
df1.tail(2) # últimas 2 linhas do DataFrame
df1.sample(2) # 2 linhas aleatórias do DataFrame
df1.info() # informações sobre o DataFrame
df1.value_counts() # conta os valores do DataFrame
df1.isnull() # verifica valores nulos no DataFrame
df1.dropna() # remove linhas com valores nulos
df1.fillna(0) # preenche valores nulos com 0
df1.replace({'F': 'Feminino', 'M': 'Masculino'}) # substitui valores no DataFrame
df1.apply(lambda x: x + 1 if x.name == 'Idade' else x) # aplica uma função em cada coluna
df1.groupby('Sexo').mean() # agrupa por 'Sexo' e calcula a média

#outros métodos
head(n)# retorna as primeiras n linhas do DataFrame.
tail(n)# retorna as últimas n linhas do DataFrame.
info()# exibe um resumo conciso do DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória.
value_counts()# conta a frequência de valores únicos em uma coluna.
isnull()# retorna um DataFrame booleano indicando a presença de valores nulos.
dropna()# remove linhas ou colunas com valores nulos.
fillna(value)# preenche valores nulos com um valor especificado.
apply(func)# aplica uma função ao longo de um eixo do DataFrame (linhas ou colunas).
groupby(by)# agrupa o DataFrame por uma ou mais colunas e permite a aplicação de funções agregadas.

import pandas as pd
dados = {
'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
'Matemática': [85, 92, 78, 90, 88],
'Física': [80, 95, 82, 88, 91],
'Química': [78, 89, 85, 87, 90]
}
df = pd.DataFrame(dados)
print(df)
# calcular a média das notas em cada disciplina usando o método mean() e desvio padrão usando o método std().
medias = list(df[['Matemática','Física','Química']].mean())
desviosp = list(df[['Matemática','Física','Química']].std())
print(medias)
print(desviosp)
#Criar um novo DataFrame com as médias e desvios padrão
mean_std = pd.DataFrame([medias, desviosp], columns=['Matemática','Física','Química'], index=['Média', 'Desvio Padrão'])
print(mean_std)

#operações com matrizes
add()# soma dois DataFrames ou um DataFrame e um escalar.
sub()# subtrai dois DataFrames ou um DataFrame e um escalar.
mul()# multiplica dois DataFrames ou um DataFrame e um escalar.
div()# divide dois DataFrames ou um DataFrame e um escalar.
pow()# eleva os elementos de um DataFrame a uma potência especificada.
eq()# verifica a igualdade entre dois DataFrames ou entre um DataFrame e um escalar.
ne()# verifica a desigualdade entre dois DataFrames ou entre um DataFrame e um escalar.
dot()# realiza o produto escalar entre dois DataFrames.

import pandas as pd
df1 = pd.DataFrame([ [19, 23, 34],
[15, 55, 60],
[7, 32, 15] ])
print(df1)

df2 = pd.DataFrame([ [2, 3, 4],
[5, 6, 7],
[8, 9, 10] ])
print(df2)

df3 = df1.add(df2) # Soma df1 e df2
print(df3)

df4 = df1.mul(2) # Multiplica df1 por 2
print(df4)

#Transformação em Matriz NumPy
#Para transformar um DataFrame em uma matriz NumPy, podemos usar o atributo to_numpy.
#Esse atributo retorna os dados do DataFrame como uma matriz NumPy.
dados = [('Ana', 21), ('Bruno', 20), ('Carla', 22)]
df = pd.DataFrame(data = dados, columns=['Nome', 'Idade'])
print(df)

matriz = df.to_numpy()
print(matriz)

#Exemplo de como transformar uma coluna específica de um DataFrame em uma matriz NumPy
print(df.loc[:, 'Idade'].to_numpy())
print(df.loc[:, 'Nome'].to_numpy())
#ou
print(df['Idade'].to_numpy())
print(df['Nome'].to_numpy())

#Exportando dados
to_csv()# exporta o DataFrame para um arquivo CSV.
to_excel()# exporta o DataFrame para um arquivo Excel.
to_json()# exporta o DataFrame para um arquivo JSON.
to_sql()# exporta o DataFrame para uma tabela em um banco de dados SQL.

import pandas as pd
dados = [('Ana', 21), ('Bruno', 20), ('Carla', 22)]
df = pd.DataFrame(data = dados, columns=['Nome', 'Idade'])
print(df)
df.to_csv('dados.csv', index=False) # Exporta o DataFrame para um arquivo CSV sem o índice

#Importando dados
read_csv()# importa dados de um arquivo CSV para um DataFrame.
read_excel()# importa dados de um arquivo Excel para um DataFrame.
read_json()# importa dados de um arquivo JSON para um DataFrame.
read_sql()# importa dados de uma tabela em um banco de dados SQL para um DataFrame.

#a partir de um site
import pandas as pd
import ucimlrepo
from ucimlrepo import fetch_ucirepo
student_performance = fetch_ucirepo(id=320)
df = pd.concat([student_performance.data.features, student_performance.data.targets], axis=1)

print(df.head()) # Mostra as primeiras linhas do DataFrame
print(df.tail()) # Mostra as últimas 5 linhas do DataFrame
print(df.info()) # Mostra informações sobre o DataFrame
print(df.describe()) # Mostra estatísticas descritivas do DataFrame

#selecionar uma das colunas do DataFrame e calcular a média e o desvio padrão dos valores
import pandas as pd
import matplotlib.pyplot as plt
df.age.mean()
df.age.std()

# plotar um histograma da coluna selecionada.
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 2)) # Altura e largura da figura
plt.hist(df.age, bins=10)
plt.title('Histograma da Idade dos Alunos')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()
#boxplot
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 2))
plt.boxplot(df.age, vert=False)
plt.title('Boxplot')
plt.ylabel('Idade dos Alunos')
plt.show()
#gráfico de dispersão (scatter plot) entre duas colunas do DataFrame.
plt.figure(figsize=(5, 4)) # Altura e largura da figura
plt.scatter(df.age, df.studytime)
plt.title('Gráfico de Dispersão: Idade vs Tempo de Estudo')
plt.xlabel('Idade')
plt.ylabel('Tempo de Estudo (horas por semana)')
plt.show()
#gráfico de barras (bar plot) para visualizar a contagem de uma coluna categórica do DataFrame.
import matplotlib.pyplot as plt
plt.figure(figsize=(5, 4)) # Altura e largura da figura










