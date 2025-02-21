"""
range() é uma função da linguagem Python que gera uma sequência (fixa) de números> É muito usada em associação a lista e á instrução for.
"""

#1) range() com *UM*pâmetro
#   Gera uma sequência numérica que vai de 0 (zero) até  valor do parâmetro -1
for num in range(10):
    print(num)

print('-' * 80)

#2) range() com *DOIS* parâmetros
#   1° parâmetro: valor inicial da sequência
#   2° parâmetro: valor final da seqência (*NÃO INCLUIDO*)
for x  in range(10,17):
    print(x)

print('-' * 80)

#3) range() com *TRÊS* parâmetros
#   1° parâmetro: valor inicial
#   2° parametro: valor final (*NÃO INCLUIDO*)
#   3° parâmetro: valor do passo (intervalo entre um número e o seguinte)

for n in range(0,22,3):
    print(n)

print('-' * 80)


# range() com passo negativo (contagem regressiva)
for i in range (10,0, -1):
    print(i)

