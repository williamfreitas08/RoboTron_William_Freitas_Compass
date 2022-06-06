#Construa um programa que recebe 20 valores para X e no final 
# apresenta a média aritmética dos valores pares digitados

pares = []
valorlist = []
media = 0

for i in range(0, 21):
    valor = int(input("Digite o numero: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        valorlist.append(valor)
media = sum(pares)/len(pares)
print("A média dos Valores PARES é:", media)


