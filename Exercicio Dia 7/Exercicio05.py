#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
with open("d:/Desktop/RoboTron_William_Freitas_Compass/Exercicio Dia 7/json/GxdV3pRP.json", encoding="utf-8") as campeonato:
    jogo = json.load(campeonato)   
print(jogo)
