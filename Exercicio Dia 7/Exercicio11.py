import pandas as pd

arquivo = pd.read_csv("d:/Desktop/RoboTron_William_Freitas_Compass/Exercicio Dia 7/csv/LndbVMRT.csv", encoding='UTF-8', sep=",")

print(arquivo[arquivo["Year"] == 1993])

nome = arquivo.loc[65, "Name"]

print("Nome do Ator:", nome)