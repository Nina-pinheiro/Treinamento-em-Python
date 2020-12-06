'''Script que eu realizo exercícios para treinar lógica de programação
Nome: Nina 

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


#6Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

# Loop 
for numero in range(1,21):
  print(numero)
 
print(list(range(1,21)))

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50

for num_impar in range (1,51,2):
  print(num_impar)

#7Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo

numero = int(input("Digite um número"))
lista=[]
resultado =1
for fatorial in range(1,numero+1):
  resultado = resultado*fatorial
  
  
print(resultado)

#8Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
#A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
#pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e 
#depois calcular a média com as notas restantes). As notas não são informados ordenadas. 


# Pedir o nome
nome = str(input("Digite o seu nome: "))
lista = []

# Loop que vai pedir 7 vezes a nota
for i in range(1,8):
  nota = int(input(f'Digite a {i}° nota : '))
  lista.append(nota)

maior_nota = max(lista)
menor_nota = min(lista)

# Remove a maior nota
lista.remove(maior_nota)
# Remove a menor nota
lista.remove(menor_nota)
# Verifica o tamanho da lista
quantidade = len(lista)
# Faz a soma das notas
soma_das_notas = sum(lista)
# Faz a media das notas
media = soma_das_notas/quantidade

print(f'Resultado final:')
print(f'Atleta: {nome}')
print(f'Melhor nota: {maior_nota}')
print(f'Pior nota: {menor_nota}')
print(f'Média: {media}')
