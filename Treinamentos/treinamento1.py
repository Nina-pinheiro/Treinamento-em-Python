"""
Treine conceitos básicos de leitura de arquivos

Autora: Nina Pinheiro 
Data: 10/05/2020 
"""


# Abrindo o arquivo para leitura em formato csv

segundo_arquivo = open("arquivos/arq2.csv","r")

# Ler o arquivo para leitura em formato csv

print(segundo_arquivo.read())

# Contar a quantidade pelo metodo "tell"

print(segundo_arquivo.tell())

# Grava o arquivo no objeto data e consegue ler
data = segundo_arquivo.read()

# Dividir o arquivo com base em critério(no caso linha)usando o método "split"

rows = data.split('\n')

print(rows)

# Outra forma de abrir o arquivo csv é por pandas

import pandas as pd

file_name = "arquivos/arq2.csv"

# Aqui você consegue ler o arquivo pelo pandas
df = pd.read_csv(file_name)

# Consegue ler os primerios arquivos
df.head()





