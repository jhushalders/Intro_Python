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











