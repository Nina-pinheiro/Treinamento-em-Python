# Concatenar sentenças

frase1 = "A insustentável leveza"
frase2 = " do ser é um livro"

print(frase1+frase2)

# Imprimindo as posições dos caracteres

frase1[0:10]

# Para sabermos o quantoa elementos tem a frase, podemos usar a função len

len(frase1)

# Se quiser saber quantas vezes ocorre a palavra "livro" utilizamos o count

frase1.count('livro')

# Se quiser colocar todas as palavras em maisculula

frase2 = frase2.upper()
frase2

# Se quiser colocar todas as palavras em minusculo

frase1 = frase1.lower()
frase1

# Encontrar o índice de onde começa determinada palavra, por exemplo 'LIVRO'

frase2.index('LIVRO')

# Uma outra função é o join que pode unir dois elementos de uma lista e transformá-lo em uma única lista

lista = ['Cientista', 'de dados']
' '.join(lista)

