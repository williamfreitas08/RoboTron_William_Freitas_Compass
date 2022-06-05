# 3- Construa um programa que recebe dois valores, soma esses valores e 
# apresenta se o resultado é par ou impar

print("PROGRAMA PARA IDENTIFICAÇÃO NÚMERO PAR OU IMPAR")

numero1 = int(input("Digite o Primeiro Numero: "))
numero2 = int(input("Digite o Segundo Numero: "))

if (numero1 + numero2)% 2 == 0:
    print("Esse numero e PAR!")
else:
    print("Esse numero e IMPAR!")
