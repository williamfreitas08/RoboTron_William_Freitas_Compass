import pandas as pd

arquivo = pd.read_csv("Arquivos_Json/LndbVMRT.csv", encoding='UTF-8', sep=",")

print(arquivo[arquivo['Movie'] != "The Revenant"])