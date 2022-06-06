from socket import SOMAXCONN



def media():
    valor1 = int (input("Digite o Primeiro Numero: "))
    valor2 = int (input("Digite o Segundo Numero: "))
    
    soma = valor1+valor2

    mediavalor = (soma)/2

    return (mediavalor)
print(" A media dos Valores Digitados é:", media())
