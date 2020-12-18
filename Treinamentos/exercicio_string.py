# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo

string1 = "O mundo não é bom, mas você não precisa ser igual a ele"
string2 = "O sol nasce para todos"

print(f' O contéudo da primeira string é: {string1}, O tamanho dela é:  {len(string1)}')
print(f'O conteúdo da segunda string é: {string2}, O tamanho dela é {len(string2)}')

if len(string1) == len(string2):
  print("As duas strings apresentam o mesmo comprimento")
else:
  print("As duas strings não apresentam o mesmo comprimento")

if string1 == string2:
  print("As duas strings apresentam o mesmo conteúdo")
else:
  print("As duas strings não apresentam o mesmo conteúdo")


#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = str(input("Digite o seu nome: "))

# inverter

nome_invertido = nome[::-1]
nome_maisculo = nome_invertido.upper()

print(nome_maisculo)

# Mais direto

print(nome[::-1].upper())


#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = str(input("Digite o seu nome: "))


for letra in nome:
  print(letra)


# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.


frase = str(input("Digite uma frase: "))

vogais = 0
espaco = 0
consoantes = 0
for caracter in frase:
  if caracter in 'aeiou':
    vogais = vogais + 1
  if caracter in '':
    espaco = espaco + 1
  else:
    consoantes = consoantes + 1
  


print(f'A quantidade de vogais é {vogais}')
print(f'A quantidade de espaços em brancos na frase é {espaco}')


