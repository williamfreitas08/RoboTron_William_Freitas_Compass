#Crie um programa que recebe 15 valores e armazena em uma lista, e no final 
#da execução mostre os valores da lista do ultimo para o primeiro

from audioop import reverse

def armazenar():
    tamanholista=3
    lista = []

    while len(lista) <= tamanholista:
        n = int(input("Digite um numero: "))
        lista.append(n)
    lista.reverse()
    print("Os Valores inseridos pelo Usuário foram: ", lista)
armazenar()


