import pandas as pd

arquivo = pd.read_csv("Arquivos_Json/LndbVMRT.csv", encoding='UTF-8', sep=",")

arquivo ["Year"] = arquivo["Year"].apply(str)

arquivo["Year_e_Movie"] = arquivo["Year"] +" "+ arquivo["Movie"]

print(arquivo.to_string())