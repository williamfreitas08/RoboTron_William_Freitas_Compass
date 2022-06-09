import pandas as pd

arquivo = pd.read_csv("Arquivos_Json/LndbVMRT.csv", encoding='UTF-8', sep=",")

coluna = pd.DataFrame(arquivo, columns= ["Year", "Name"])

nova_coluna = coluna[(coluna.Year == 1991) | (coluna.Year == 2016)].loc[:,"Name"]

print(nova_coluna)

