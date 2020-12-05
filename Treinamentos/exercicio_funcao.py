'''Script que eu realizo exercícios para treinar lógica de programação
Nome: Nina 

Exercícios sobre Funções

'''

# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


# Função que retorna a soma dos 3 valores
def soma (x,y,z):
  soma = x + y + z

  return soma

# Declaração de variáveis
a = float(input("Digite o primeiro numero"))
b = float(input("Digite o primeiro numero"))
c = float(input("Digite o primeiro numero"))

# Printando o número e chamando a função
print(' A soma dos três números é = ', soma(a, b, c))


# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

# Função que retorna o caracter
def caractere(x):
  if x > 0:
    x = "P"
  else:
    x = "N"

  return x

# Declaração de variável
a = int(input("Digite um número"))

# Chamando a função
caractere(a)


#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
#sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

# Função Soma imposto que vai retornar o custo
def somaImposto(taxaImposto,custo):

  custo = custo * (1-taxaImposto)/100

  return custo


cost = float(input("Digite o custo"))
taxa = float(input("Digite a taxa de imposto"))

# Chamando a função
somaImposto(cost,taxa)



# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

# Função que vai retornar o tamanho do digito - cuidando aqui é que a variável tem que ser strinf
def quantidade(digito):

  

  return len(digito)

num = str(input("Digite a quantidade de digitos"))

# Chamando a função
quantidade(num)