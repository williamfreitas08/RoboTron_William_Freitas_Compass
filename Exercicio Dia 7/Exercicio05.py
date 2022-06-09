#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
with open("Arquivos_Json/GxdV3pRP.json", encoding="utf-8") as campeonato:
    jogo = json.load(campeonato)   
print(jogo)
