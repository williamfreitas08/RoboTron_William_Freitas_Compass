#Construa um programa que receba um valor inteiro 
#maior que 2 em uma variavel X e apresenta os impares entre 0 e x
  
from numpy import sort

numero = int(input("Digite um numero MAIOR que 2: "))

if numero > 2:
    impar = []
    for i in range(numero, 0, -1):
        if i % 2 == 1:
            impar.append(i)
    impar.sort()
print( "Os numeros IMPARES entre 0 e", {numero}, "são", impar)

