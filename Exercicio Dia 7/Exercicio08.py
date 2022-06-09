#Importa a biblioteca PANDAS
import pandas as pd

manipulacao = "Arquivos_Json/LndbVMRT.csv"

primeiro_arquivo = pd.read_csv(manipulacao, encoding='UTF-8', sep=',')

print(primeiro_arquivo.to_string())


