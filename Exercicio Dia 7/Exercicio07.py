#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
def valor_json():
    with open('d:/Desktop/RoboTron_William_Freitas_Compass/Exercicio Dia 7/json/GxdV3pRP.json',encoding="utf-8") as campeonato:
        campeonato1 = json.load(campeonato)
        return campeonato1   
dados_campeonato= valor_json()

for valores in dados_campeonato:
   print(valores)

