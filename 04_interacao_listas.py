frutas = ["laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibit apenas seus elementos, usamos a estrutura for...in, como já visto no arquivo n° 2
print("Percurso normal:")
for f in frutas:
    print(f)

print("-" * 80)

# Percorrendo a lista em ordem reserva: reversed()
print("Percurso reverso")
for x in reversed(frutas):
    print(x)

print("-" * 80)

# No entanto, é comum precisar exibir, além do valor do elemento, também sua posição na lista. Nesse caso, devemos usar a estrutura for... in combinada com as funções range()
# e len()
print("Percurso mostrando posição e valor")
for pos in range(len(frutas)):
    print(f"Posição {pos} => {frutas[pos]}")

print("-" * 80)

# Ás vezes é necessário percorrer a lista de trás para frente, mas tendo acesso também ás posições dos elementos. Para isso, usamos a estrutura for...in, lent()
# e range() com três parâmetros
print("Percuso inverso mostrando posição e valor:")
for p in range(len(frutas)-1, -1, -1):
    print(f"Posição {p} => {frutas[p]}")
