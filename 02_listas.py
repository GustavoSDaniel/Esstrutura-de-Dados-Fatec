"""" Lista é uma estrutura de dados nativa da linguagem python. Ela permite que varios valores sejam associados a uma unica variavel. """

#Lista de strings

frutas = ["maça", "morango", "laranja", "uva", "manga" "goiaba"]

# Lista De números 

nums = [3,10,-7,12.8,-0.5,4,22]

#Lista com valores de varios tipos (pouco comum)
mistureba = ["Joaquim", 37, 1.81,79, True]

### OPERAÇÕES SOBRE LISTAS

#1) PERCURSO
#Percorrer uma lista significa visitar cada um dos seus itens e fazer algo com ele. No exemplo a seguir, vamos dar print() em cada uma das frutas da lista ###

for f in frutas:
    print(f)

#Traça separador
print("-" * 80)

#Percorre a lista de numeros exibindo o propio numero e seu valor elevado a 2 

for num in nums:
    print(f"{nums} => {num ** 2}")

print("-" * 80)


# 2) Inserção de um novo elemento no *FIM* DA LISTA: append()

print("frutas, ANTES:", frutas)
print("nums, ANTES:", nums)

# Inserindo novos itens ao final da listas
frutas.append("maracujá")
nums.append(19)

print("frutas, DEPOiS:", frutas)
print("nums, DEPOIS:", nums)

print("-"*80)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º -> a posição onde será feita a inserção (A CONTAGEM COMEÇA EM ZERO)
#    2º -> o novo elemento a ser inserido

#Inserindo um novo elemento na PRIMEIRA posição
frutas.insert(0,"melancia")

#Inserindo um novo elemento na QUARTA posição
frutas.insert(3,"amora")

print(frutas)

print("-" * 80)

