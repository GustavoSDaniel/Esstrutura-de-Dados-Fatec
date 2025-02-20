"""" Lista é uma estrutura de dados nativa da linguagem python. Ela permite que varios valores sejam associados a uma unica variavel. """

#Lista de strings

frutas = ["maça", "morango", "laranja", "uva", "manga", "goiaba"]

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

#4) ACESSANDO VALORES, INFORMANDO A RESPECTIVA POSIÇÃO
print("Eleento da QUINTA posição:", frutas[4])
print("Eleento da PRIMEIRA posição:", frutas[0])
print("Eleento da ULTIMA posição:", frutas[-1])
print("Eleento da PENULTIMA posição:", frutas[-2])

#5) SUBSTITUINDO VALORES EXISTENTES
print("ANTES:", frutas)

#Substituindo o valor da posição 3 (QUARTA posição)
frutas[3] = "Framboesa"
#Substituindo o valor da posição 0 (PRIMEIRA posição)
frutas[0] = "Pitanga"
#Substituindo o valor da posição -1 (ULTIMA posição)
frutas[-1] = "Melão"

print("DEPOIS:", frutas)

#6) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()
print("Quantidade de elementos da lista de frutas:", len(frutas))
print("Qantidade de elementos da lista de números:", len(nums))

print("-" * 80 )

#7) REMOVENDO O *ULTIMO* O ULTIMO ELEMENTO DE UMA LISTA: pop() (sem parametrro)
print("ANTES:", frutas)
removido = frutas.pop()
print("Valor removido:", removido)
print("DEPOS:", frutas)

print("-" * 80 )

#8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() (COM parametro)
print("Removendo elemento da posição 3...")
removido = frutas.pop(3)
print(frutas)

print("-" * 80 )


#9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
print("Removendo 'uva'...")
frutas.remove("uva")
print(frutas)


#10) AUMENTANDO UMA LISTA COM ELEMENTOS DE OUTRA LISTA: extend()
maisFrutas = ['carambola', 'pera', 'acerola', 'jabuticaba', 'caqui']
frutas.extend(maisFrutas)
print("Adicionando mais frutas álista... ")
print(frutas)

#11) FATIANDO UMA LISTA
#  Fatiar significa copiar um pedaço de uma lista (sublista)
# criando uma nova lista

#Criar uma nova lista com os elementos das posições de 2 a 5 (posição # 6 *NÃO ENTRA*) da çista de frutas
subLista2a5 =  frutas[2:6]
print("Sublista com as frutas das posições de 2 a 5:")
print(subLista2a5)

# Crie uma sublista que contém os elementos desde o inicio atẃ a posição # 6 (posição 7 *NÃO ENTRE*) 
subListaAte6 = frutas[7]
print("Sublista do inicio até a posição 6:")
print(subListaAte6)

#Crie um sublista qie contém s elementos desde a posição 5 até o final
sublistaDesde5 = frutas[5]
print("Sublista da posição 5 até o final:")
print(sublistaDesde5)