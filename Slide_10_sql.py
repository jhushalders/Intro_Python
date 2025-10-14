#SQL
#CREATE, ALTER, DROP #criar e modificar estruturas de tabelas
#SELECT #consultar dados
#INSERT #inserir dados
#UPDATE #atualizar dados
#DELETE #deletar dados
#JOIN #combinar dados de duas ou mais tabelas
#UNIO #combinar resultados de duas ou mais consultas SELECT
#MIN, MAX, AVG, SUM #funções agregadas para cálculos
#WHERW #filtrar resultados com operadores = != LIKE IN BETWEEN
#Colunas #possui tipo de dado específico conhecido como "domínio de dados" (TEXT, INTEGER, REAL)
#Linhas #representa uma única entrada ou registro na tabela
import pandas as pd
import numpy as np

df = pd.read_cvs('cursos.csv')
print(df.head())#exibe as 5 primeiras linhas do dataframe
