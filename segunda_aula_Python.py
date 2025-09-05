library
#LISTAS
L1= [1, 3, 50, [19, 20, 21],34, "texto"] #primeiro valor índice 0
L1[0]
L1[3][1] #acessar a lista dentro da lista
L1[5]

#alterar o elemento
L1[0]=2
L1

#fatiamento  sequencia[inicio:fim:passo] índices funcionaem igual as strings [)
L1[2:5:2]
L1[2:5]

#funções listas
L = [10, 20, 30, 40]
len(L) #retorna o tamanho da lista

min(L) #menor valor

max(L)#maior valor

sum(L) #soma de todos os elementos

L.append(50) #adiciona novo valor no final
L

L.extend([50, 60]) #adiciona mais valores ao final
L

del L[1] #remove elemento pelo índice
L

30 in L #verifica se pertence a lista

L.sort() #ordenar em ordem crescente
L

L.reverse() #inverte os elementos
L

#concatenação
A = [10,20,30]
B = [40,50,60]
C = A + B
print(C)

#repetição
L = [1,2]
R = L * 4
print(R)

#função range()
L3 = list(range(2))#gera valores de 0 ate 1
L3
L4 = list(range(2,5)) #gera valors de 2 até 4
L4
L5 = list (range(2,10,2)) #gera valores de 2 a 9, pulando 2 a 2
L5

#TUPLAS
#Uma tupla é semelhante a uma lista, mas imutáve
T = (1, 2, 3, 4, 5)
print(T)

#Podemos extrair valores de uma tupla diretamente em variáveis

T = (10, 20, 30, 40, 50)
a, b, c, d, e = T
print("a =", a, "b =", b)
print("d+e =", d+e)

#DICIONÁRIO
#chave:valor
aluno = {"nome": "Ana", "idade": 20, "curso": "Estatística e Ciência de Dados"}
print(aluno)

carro = dict(marca="Fiat", modelo="Uno", ano=2015)
carro

#para acessar, usamos a CHAVE
print(carro["marca"])
print(carro.get("ano")) #A diferença é que get() não gera erro se a chave não existir, retorna None.

# Alterar valor
carro["ano"] = 2021
# Adicionar novo par chave:valor
carro["cor"] = "prata"
# Remover chave
del carro["modelo"]
print(carro)

#Também podemos verificar se uma chave existe:
print("marca" in carro) # True
print("modelo" in carro) # False

aluno = {"nome": "Ana", "idade": 20, "curso": "Estatística e Ciência de Dados"}

# Retorna todas as chaves
print(aluno.keys())

# Retorna todos os valores
print(aluno.values())

# Retorna pares (chave, valor)
print(aluno.items())

print(len(aluno)) # retorna quantos pares chave:valor existem.
aluno.pop("idade") # remove a chave e retorna o valor associado à chave.
aluno
aluno.clear() #apaga todo o conteúdo do dicionário
aluno










