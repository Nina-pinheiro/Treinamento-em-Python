'''Script que eu realizo exercícios para treinar lógica de programação
Nome: Nina 

Exercícios sobre Listas

'''

#1.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = [1,8,9,10,5,100,15,16,17,20]

vetor.sort(reverse = True)

print(vetor)

#2.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for i in range(0,5):
  numero = int(input(f'Digite o numero: '))
  vetor.append(numero)
 

print(vetor)

# 3.Faça um programa que leia 5 valores números e guarde-os em uma lista. No final mostra qual foi o maior 
#e o menor valor digitado na lista


lista = []

for i in range(0,5):
  lista.append(int(input(f'Digite um valor para a Posição {i}')))

print(f'Voce digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}')
print(f'O maior valor da lista é {min(lista)}')