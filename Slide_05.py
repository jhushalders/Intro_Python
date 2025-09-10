#ESTRUTURAS DE CONTROLE
#ESTRUTURAS DE DECISÃO
nota = float(input("Digite a nota:"))
4
if nota >= 7:
  print ("Aluno aprovado")
elif nota >= 4:
  print ("Exame")
else:
  print ("Aluno reprovado")

n = 13
if n > 0:
  print ("número positivo")
elif n == 0:
  print ("número igual a 0")
else:
  print("número negativo")

!= #diferente
and
or
not

#ESTRUTURA DE REPETIÇÃO
#while: nao sabemos quantas vezes vai repetir
#for: quantidade conhecida de repetição

contador = 0
while contador < 5:
  print ("Contador:", contador)
  contador += 1

senha = "54321"
leitura=""
while leitura != senha:
  leitura = input("Digite a senha: ")
  if leitura == senha:
    print ("Acesso liberado")
  else:
    print ("Senha incorreta. Tente novamente")
    
x = 0
while x < 5:
  print (f"O valor de x é {x}")
  x +=1

for i in range(5):
  print(i)

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
 print("Eu gosto de", fruta)


#For com range(início, limite, passo)
S = 0
for x in range(1, 20, 3):
 S = S + x
print("Soma =", S)

notas = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
soma = 0
for nota in notas:
 soma += nota
media = soma / len(notas)
print("Média =", media)

S = 0  
for x in range(3, 334, 3):
 S += x
print("Soma =", S)

