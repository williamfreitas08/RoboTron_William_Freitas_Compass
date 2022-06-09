import pandas as pd

tabela = pd.read_csv("Arquivos_Json/Tabela_Periodica.csv", encoding="utf-8", sep=";")

def propriedades():
    opcao = str(input('''
*****************************************************************
                    ESCOLHA UMA OPÇÃO
Propriedades:

[1]Nome
[2]Numero_Atomico    
[3]Linha
[4]Coluna
[5]Estado_Fisico

******************************************************************
ESCOLHA UMA OPÇÃO ACIMA:
'''))

    if opcao == "1":
        Nome()
    elif opcao == "2":
        Numero_Atomico()
    elif opcao == "3":
        Linha()
    elif opcao == "4":
        Coluna()
    elif opcao == "5":
        Estado_Fisico()

def Nome():
    for i in range(0, len(tabela)):
        print(tabela.iloc[i]["Nome"])
def Numero_Atomico():
    for i in range(0, len(tabela)):
        print(tabela.iloc[i]["Num_Atomico"])
def Linha():
    for i in range(0, len(tabela)):
        print(tabela.iloc[i]["Linha"])
def Coluna():
    for i in range(0,len(tabela)):
        print(tabela.iloc[i]["Coluna"])
def Estado_Fisico():
    for i in range(0, len(tabela)):
        print(tabela.iloc[i]["Estado_Fisico"])

def listarDados():
    try:
        dado = input("Informe o símbolo que voce deseja buscar: ")
        print(tabela[tabela["Simbolo"] == dado])
    except:
        print("OPS! Verifique se o simbolo esta correto")
    

def printDados():
    print(tabela)

def main():
    
    propriedades()
    listarDados()
    printDados()
    
main()