#Crie um programa que recebe uma lista com três frutas e compare com uma 
# lista com os valores ["maça", "banana", "pera"]

def prog_comparacao():

    lista_usuario = []
    lista_frutas=["maça","banana","pera"]
    
    
    for i in range(len(lista_frutas)):
        lista_usuario.append(input("Digite uma fruta que você procura: "))  
         
        for i in lista_usuario:
            for j in lista_frutas:
                if i==j:
                    print("Essa fruta está em Estoque! ", i)
            else:
                i != j
                print("O valor ",i)
                print("ATENÇÃO: A fruta não está em estoque! ")
    return print(lista_usuario)   
prog_comparacao()
