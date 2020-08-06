# Treinamento em Python 
# Criado por Nina Machado
# Python 3.7

# Biblioteca necessária
import numpy as np

# Criar um array a partir de uma lista 

lista_array = np.array([0,1,2,3,4])
print(lista_array)

type(lista_array)

# Calcula os valores acumulados pelo método "cumsum"
lista_array.cumsum()

# Manipulando o array, importante saber que um array é um conjunto de um mesmo tipo, 
# como o tipo é inteiro não consegue add uma string

lista_array[0] = 20
print(lista_array)

# Verificar a dimensionalidade do array

print(np.shape(lista_array))

# Função arrange cria um vetor contendo uma progressão aritmetica a partir de um intervalo start, stop e step

lista2 = np.arange(0,200,7)
print(lista2)

# Da para criar um array com a função zero, dentro do parentêse é o número de elementos de array

print(np.zeros(5))

# Criando uma array "matriz identidade", dentro do parentêse escolhe qual será a ordem.
# Retorna 1 nas posições em diagonal e 0 no restante>> Identidade

identidade = np.eye(5)
print(identidade)

# Fazer um array que eu escolho os parâmetros que irão para a diagonal

diagonal = np.diag(np.array([10,20,30]))
print(diagonal)

# Criando um array com números complexos

complexos = np.array([1+2j,1-2j])
print(complexos)

# Criando array com valores booleanos 

bool = np.array([True,False])
print(bool)

# Criando array com strings

string = np.array(['Science','Flor'])
print(string)

