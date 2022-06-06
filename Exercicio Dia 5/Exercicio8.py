# Crie um programa que lê 1 valor inteiro para X. Se o valor for par, 
# calcular o fatorial de x em uma função e apresentar o resultado fora da função. 
# Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.

def exercicio8():

    numero = int(input('Digite um numero inteiro: '))
    calc_fatorial = 1
    result = 1
    cont = 1

    if (numero % 2) == 0:
        print("Atenção seu número é um fatorial: ")
        while cont <= numero:
            calc_fatorial = calc_fatorial * cont
            cont = cont + 1
        print(" Seu fatorial é ",calc_fatorial)
    else:
        print("Seu numero é IMPAR e sua TABUADA: ")
        for i in range(1, 11):
            mult = i * numero
            print(i , ' x ', numero, ' = ', mult)
exercicio8()

