import pandas as pd

arquivo = pd.read_csv("Arquivos_Json/LndbVMRT.csv", encoding='UTF-8', sep=",", usecols=["Age"])

print(arquivo.to_string())
