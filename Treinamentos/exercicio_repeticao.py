'''Script que eu realizo exercícios para treinar lógica de programação
Nome: Nina M.I.S.P.Machado

Exercícios sobre Estrutura de Repetição

'''


# 1)Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 a 10: "))

while (nota<0 or nota>10):
  nota=float(input('Digite uma nota entre 0 a 10'))

else:
  exit()

#2)Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Digite o seu nome:"))
senha = str(input("Digite a sua senha:"))

while nome == senha:
  print("Sua senha não deve ser igual ao seu nome, por favor insira uma senha diferente")
  nome = str(input("Digite o seu nome:"))
  senha = str(input("Digite a sua senha:"))
else:
  exit()

#3 Faça um programa que leia 5 números e informe o maior número.

num = int(input('n')) 
for i in range(5) :
  numero = int(input("Digite o numero"))
  if num > numero:
    print('o número maior é:' ,num)
  else:
    print('numero maior é :',numero)
    num = numero 

# 4 Outra forma de fazer - utilizando a função max e 
# armazenando numa lista os valores

lista = []
numero = int(input("Digite um número:"))

for n in range (5):
  lista.append(int(input("Digite o número: ")))

print("O maior número da lista", max(lista))


# 5)
#Faça um programa que leia 5 números e informe a soma e a média dos números
soma= 0
media = 0
for num in range(5):
  numero = int(input())
  soma = numero + soma
  media = soma/5


print("A soma dos 5 números é ", soma)
print("A média dos 5 números é ", media)





