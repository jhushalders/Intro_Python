x = 5
print(r.y) #acessar objeto do R no Python

import math
math.sqrt(25)

import math as mt #mudar o nome do pacote
mt.sqrt(25)

type(x) #saber tipo da variável

#STRING

#CONCATENAÇÃO
nome = "Thomas"
sobrenome = "Bayes"
nome_completo = nome + " " + sobrenome
print(nome_completo)

a = 'Programação'
b = 'Python'
c = a + b
print(c)

s = "ABC"

s + "C" # 'ABCC'

s + "D" * 4 # 'ABCDDDD'

"X" + "-"*10 + "X" # 'X----------X'

s + "x4 = " + s*4 # 'ABCx4 = ABCABCABCABC'

#MANIPULAÇÃO
teste = "Introdução ao Python" #Retorna o tamanho da string.
len(teste) 

a = "python" #Retorna a string com a primeira letra maiúscula
a.capitalize()

b = "Linguagem Python" #Informa quantas vezes um caractere (ou sequência) aparece na string.
b.count("n") 

c = "Python" #Verifica se a string inicia com determinada sequência.
c.startswith("Py")

d = "Python" #Verifica se a string termina com determinada sequência. 
d.endswith("Py")

e = "!@#$%" #Verifica se a string possui apenas caracteres alfanuméricos. 
e.isalnum() 

f = "Python" #Verifica se a string possui apenas letras.
f.isalpha() 

g = "Python" #Verifica se todas as letras estão minúsculas.
g.islower() 

h = "PYTHON 12" #Verifica se todas as letras estão maiúsculas
h.isupper() 

i = "PYTHON 3" #Retorna a string com todas as letras minúsculas.
i.lower() 

j = "Python" #Retorna a string com todas as letras maiúsculas.
j.upper()

k = "Python" #Inverte o conteúdo (maiúsculas ↔ minúsculas). 
k.swapcase() 

l = "apostila de python" #Converte para maiúsculo todas as primeiras letras de cada palavra da string.
l.title() 

m = "cana de açúcar" #Transforma a string em uma lista, utilizando os espaços como referência
m.split()

n = "Apostila teste" #Substitui na string o trecho S1 pelo trecho S2.
n.replace("teste", "Python") 

o = "Python" #Retorna o índice da primeira ocorrência de um caractere. Retorna -1 se não encontrado.
o.find("h") 

p = "Python" #Ajusta a string para um tamanho mínimo, acrescentando espaços à direita.
p.ljust(15)

q = "Python" #Ajusta a string para um tamanho mínimo, acrescentando espaços à esquerda.
q.rjust(15) 

r = "Python" #Centraliza a string para um tamanho mínimo, acrescentando espaços nos dois lados.
r.center(10)

s = " Python " #Remove espaços à esquerda da string.
s.lstrip() 

t = " Python " #Remove espaços à direita da string.
t.rstrip() 

u = " Python " #Remove espaços em branco dos dois lados da string.
u.strip()

#FATIAMENTO
#começa no índice 0 e o último índice não está incluso [inf, sup)
s = "Python"

# Pega os caracteres das posições 1, 2 e 3
s[1:4]

# Pega do índice 2 até o final
s[2:]

# Pega do início até o índice 3
s[:4]

nome = "ABCDE"
nome[:-2] #ABC

#COMPOSIÇÃO
# %d → números inteiros
# %s → strings
# %f → números decimais

#Tamanho mínimo (%3d)
#Zeros à esquerda (%03d)
#Casas decimais (%5.2f)

idade = 22
print("[%d]" % idade) # [22]

print("[%03d]" % idade) # [022]

print("[%3d]" % idade) # [ 22]

print("%.2f" % 5) # 5.00

print("%30.2f" % 5) #                          5.00

idade = 22
nome = "João"
grana = 51.34
print("%s tem %d anos e R$%5.2f no bolso" % (nome, idade, grana))
#João tem 22 anos e R$51.34 no bolso
