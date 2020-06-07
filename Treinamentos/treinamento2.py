"""
Treine conceitos básicos de leitura de arquivos

Autora: Nina Pinheiro 
Data: 10/05/2020 
"""


# Abrindo o arquivo para leitura em formato TXT
primeiro_arquivo = open("arquivos/arquivo1.txt","r")

# Lendo o arquivo utilizando o método "read"
print(primeiro_arquivo.read())

print(primeiro_arquivo.readlines())
# Para contar o número de caracteres , utilizando o método "tell"

print(primeiro_arquivo.tell())

# Utilizar o método seek para retornar o início do arquivo

print(primeiro_arquivo.seek(0,0))

# Ler os primeiros caracteres que eu desejo pelo método read

print(primeiro_arquivo.read(10))

# Abrindo arquivo para gravação
primeiro_arquivo = open("arquivos/arquivo1.txt", "w")


