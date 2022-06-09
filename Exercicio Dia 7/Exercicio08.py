#Importa a biblioteca PANDAS
import pandas as pd

manipulacao = "d:/Desktop/RoboTron_William_Freitas_Compass/Exercicio Dia 7/csv/LndbVMRT.csv"

primeiro_arquivo = pd.read_csv(manipulacao, encoding='UTF-8', sep=',')

print(primeiro_arquivo)


