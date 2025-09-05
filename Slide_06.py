#FUNÇÃO ROUND arredonda números para o inteiro mais próximo
print(round(3.7))
print(round(3.14159, 2))

#FUNÇÃO MAP usada para aplicar uma função a cada item de um iterável e retornar um novo iterável com os resultados.

x = [1,-1,2,-2,3,-3] 
y = list(map(abs, x)) # Aplica a função abs(numero absoluto) a cada elemento de x
print (y)

#FUNÇÃO FILTER filtrar os elementos de um iterável com base em uma condição específica
lista = ["1","2","3","João","Maria","Paula"]
x = list(filter(str.isdigit, lista)) # Filtra apenas os elementos que são dígitos
print(x)

y = list(map(int, x)) # Converte os elementos filtrados para inteiros
print(y)

#FUNÇÃO ZIP usada para combinar elementos de múltiplos iteráveis em pares ordenados
x = [1,2,3]
y = [4,5,6]
z = [7,8,9,10]
result1 = list(zip(x,y))
result2 = list(zip(x,z))
result3 = list(zip(x,y,z))
print(result1)
print(result2)
print(result3)

#FUNÇÃO ENUMERATE usada para adicionar um contador automático a um iterável, retornando pares de índice e valor
lista = [ " Primeiro " , " Segundo " , " Terceiro " ]
lista_com_indice = list(enumerate(lista))
print(lista_com_indice)

notas = [6.5, 7.0, 8.2, 5.9, 9.1, 6.8]
# Aplica bônus de 1 ponto nas notas de posições ímpares
for i, nota in enumerate(notas):
    if i % 2 != 0:  # Verifica se o índice é ímpar
        notas[i] = min(nota + 1, 10.0)  # Adiciona 1 ponto à nota, mas não ultrapassa 10.0
print(notas)

#Manipulação de Arquivos: Conceitos Fundamentais

#Função open(nome, modo): É usada para abrir um arquivo em Python
#nome: O nome do arquivo (ex: "dados.txt")
#modo: Uma string que define a operação. Principais modos:
#'r': Leitura (read).
#'w': Escrita (write). Apaga o conteúdo anterior se o arquivo já existir.
#'a': Escrita (append). Adiciona novos dados ao final do arquivo, preservando o conteúdo existente.

#Escrevendo em um arquivo (modo='w')
#O método .write() grava uma string no arquivo. É preciso adicionar \n para criar novas linhas.
# Abre o arquivo para escrita. Se não existir, será criado.
arquivo_escrita = open("numeros.txt", "w")

# Escreve os números de 1 a 5
for linha in range(1, 6):
    arquivo_escrita.write(f"{linha}\n")

arquivo_escrita.close()  # Fecha o arquivo para salvar as alterações
print("Arquivo 'numeros.txt' criado com sucesso.")

#Lendo de um arquivo (modo='r')
#O método .readlines() lê todas as linhas do arquivo e retorna uma lista.
# Abre o mesmo arquivo, agora para leitura
arquivo_leitura = open("numeros.txt", "r")
print("\nConteúdo do arquivo:")
for linha in arquivo_leitura.readlines():
  print(linha.strip()) # .strip() remove quebras de linha invisíveis
arquivo_leitura.close()

#Adicicionando mais dados (modo='a')
# Abre o arquivo para adicionar mais números
arquivo_append = open("numeros.txt", "a")
for linha in range(6, 11): # Adiciona os números de 6 a 10
  arquivo_append.write(f"{linha}\n")
arquivo_append.close()

#CRIANDO SUA FUNÇÃO
def numero_par(numero):
  return numero % 2 == 0 # Retorna True se o número for par, caso contrário False
numeros = [1, 2, 3, 4, 5, 6]
for i in numeros:
  if numero_par(i):
    print(f"{i} é par")
  else:
    print(f"{i} é ímpar")

def funcao_exemplo(a, b=2, c=3): #caso nao col
  return a + b * c
resultado1 = funcao_exemplo(4)
resultado2 = funcao_exemplo(4, 5)
resultado3 = funcao_exemplo(4, 5, 6)
print(resultado1)
print(resultado2)
print(resultado3)

def estatisticas(lista):
  maximo = max(lista)
  minimo = min(lista)
  media = sum(lista) / len(lista)
  return maximo, minimo, media
dados = [10, 20, 30, 40, 50]

# Chamando a função e armazenando os resultados nos objetos
maximo_dados, minimo_dados, media_dados = estatisticas(dados)
print(f"Máximo: {maximo_dados}, Mínimo: {minimo_dados}, Média: {media_dados}")

#Expresões Lambda forma concisa de criar funções anônimas (sem nome)
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)

#Método função que está associada a um objeto e é chamada usando a notação de ponto (objeto.método())

x = 'Python'
y = [1,-2,-3,-4,5]
# Função:
print(x)
max(y)
# Método:
x.upper()
y.append(99)
print(y)

#PACOTES
#Matemática (math, statistics, random);
#Sistema operacional (os, sys, pathlib);
#Data e hora (datetime, time);
#Arquivos e compressão (csv, json, zipfile);
#Internet e rede (http, urllib);

import math
print(math.floor(3.7))
print(math.ceil(3.2))
print(math.trunc(-3.9))

#statistics.mean(lista) → média aritmética.
#statistics.median(lista) → mediana.
#statistics.mode(lista) → moda (valor mais frequente).
#statistics.stdev(lista) → desvio padrão amostral.
#statistics.variance(lista) → variância amostral.
import statistics as st
dados = [2, 4, 4, 4, 5, 7, 9]
st.mean(dados)
st.median(dados)
st.mode(dados)
st.stdev(dados)

import random
# Gerar um número aleatório entre 1 e 10
random.seed(19) # Define a semente para reprodutibilidade
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatório entre 1 e 10: {numero_aleatorio}")

# Gerar um número aleatório entre 0 e 1
random.seed(42) # Define a semente para reprodutibilidade
numero_aleatorio_float = random.random()
print(f"Número aleatório entre 0 e 1: {numero_aleatorio_float}")

# Selecionar um elemento aleatório de uma lista
import random
random.seed(7) # Define a semente para reprodutibilidade
elemento_aleatorio1 = random.choice(['maçã', 'banana', 'laranja','mamao','abacaxi'])
elemento_aleatorio2 = random.choice(['maçã', 'banana', 'laranja','mamao','abacaxi'])
print(f"Elementos aleatórios selecionados: {elemento_aleatorio1,elemento_aleatorio2}")

#reticulate::py_install("nome_do_pacote") dentro de um script R.
#pip install nome_do_pacote no terminal ou prompt de comando.

#No Rstudio, você pode usar a função reticulate::py_help("nome_do_pacote") para
#acessar a documentação do pacote instalado.


#Atualização: Pacotes são frequentemente atualizados para corrigir bugs ou adicionar novas
#funcionalidades. Mantenha seus pacotes atualizados para aproveitar essas melhorias.
#Ou no Rstudio: reticulate::py_install("nome_do_pacote", pip = TRUE, upgrade =
#TRUE)







