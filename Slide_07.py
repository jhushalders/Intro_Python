#ARRAYS
#Python base
#coleções homogêneas
#não otimizado para operações matemáticas
import array
#sintaxe: array.array('typecode', [elementos])
#typecode: 'i' (inteiros), 'f' (float), 'd' (double), 'u' (unicode)
numeros_inteiros = array.array("i", [1, 2, 3, 4, 5])
type(numeros_inteiros)
print(numeros_inteiros)
#criando uma lista de floats
numeros_reais = array.array("f", [1.5, 2.5, 3.14, 3.5])
print(numeros_reais)
#tentar usar tipos mistos
misto = array.array("i", [1, 2.5, 3, 4.0,"texto"]) #vai dar erro

#indexação, slicing e laços
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
a[0]
a[-1]
a[:3]
a[1:4]
a[::2]

for x in a:
  print (x)

for i in range(len(a)):
  print(i,a[i])

#modificando elementos
a[1] = 99 #modifica o segundo elemento
a.append(60) #adiciona um elemento no final
a.extend([70,80]) #adiciona vários elementos no final
a.insert(2, 25) #insere o valor 25 na posição 2
a.remove(30) #remove o valor 30
a.pop(2) #remove o elemento na posição 2
print (a)

b = arr.array('i', [10, 20, 30])
print(f"Saída: {b*2}")
print(f"Saída: {b+b}")

#operações só com loop
resultado = arr.array('i', [x*2 for x in b])
print(f"Saída: {resultado}")

#NumPy
#reticulate:: py_install("numpy") no R
import numpy as np
A = np.array([[[1, 2], [3, 4]],
             [[5, 6], [7, 8]],
             [[9, 10], [11, 12]]])
print(A)
print(A[0][0][0])
print(A[1,1,1])
print(A.shape) #dimensões
print(A.ndim) #número de dimensões
print(A.size) #número de elementos
print(A.dtype) #tipo dos elementos

#contas
y = np.array([1, 2, 3], dtype=float) #pode especificar o tipo
w = np.array([4, 5, 6])
resultado = y + w
print(resultado)
resultado = y *3+ w
print(resultado)

#slicing igual de listas

#mascara booleana: elementos maiores que 2
a = np.array([1, 2, 3, 4, 5])
masc = a > 2
print(masc)
print(a[masc])
print(a[a > 2])
#ou direto
print(a[a % 2 == 0]) #pares
print(a[a % 2 != 0]) #ímpares
print(np.sqrt(a)) #raiz quadrada
print(np.log(a)) #logaritmo

#operações entre matrizes
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
print ("A@a2 =\n", a1 @ a2) #multiplicação de matrizes

#função reshape
a = np.arange(12) #array com 12 elementos
print(a)
b = a.reshape(3, 4) #3 linhas e 4 colunas
print(b)

b[0,0] = 99 #modifica o elemento na posição (0,0)
print(b)
print(a) #o array original também foi modificado

#add linha
nova = np.array([10, 11, 12, 13])
b = np.vstack([b, nova])
print(b)

#concatenar arrays
c = np.array([[20, 21, 22, 23]])
d = np.concatenate([b, c], axis=0) #axis=0 para linhas, axis=1 para colunas
print(d)

#remover linha
e = np.delete(d, 0, axis=0) #remove a primeira linha
print(e) #axis=1 remove coluna

#broadcasting
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 0, 1])
C = A + B
print(C)

#FUNÇÕES no NumPy
a = np.array([1, 2, 3, 4, 5])
print(np.sum(a)) #soma
print(np.mean(a)) #média
print(np.median(a)) #mediana
print(np.std(a)) #desvio padrão
print(np.var(a)) #variância
print(np.min(a)) #mínimo
print(np.max(a)) #máximo






