#Construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, 
# apresenta "Maior de idade", se a idade for menor que 12, apresenta "Você é uma criança" e se for 
# maior que 12 e menor que 18, apresenta "Você é um adolescente

idade = int(input("Digite sua Idade: "))

if idade > 18:
    print("Voce e MAIOR DE IDADE")
if idade < 12:
    print("Voce e UMA CRIANCA!")
if (idade > 12) and (idade < 18):
    print("Voce e ADOLESCENTE!")