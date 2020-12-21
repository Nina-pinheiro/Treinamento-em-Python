"""
Treine conceitos básicos de leitura de arquivos

Autora: Nina Pinheiro 

"""


# Criação de um arquivo json - aba "dados.json"
# JSON (JavaScript Object Notation) é uma maneira de armazenar informações de forma organizada e de fácil acesso

dict = { 'nome' : 'Nina Machado',
         'linguagem' : 'Python',
         'similar' : ['c', 'Modula-3', 'lisp'],
         'users' : 1000000}

# Abrir arquivos JSON

import json

# Converter um dicionário para um objeto Json

json.dumps(dict)

# Criando um arquivo Json
with open ('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))

# Leitura de arquivos em Json

with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)

# Imprimindo um arquivo Json diretamente da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json"). read().decode('utf8')
datas = json.loads(response)[0]

print ('Título: ', datas['title'])
print ('URL: ', datas['url'])
print ('Duração: ', datas['duration'])
print ('Número de Visualizações: ', datas['stats_number_of_plays'])



