#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
with open("Arquivos_Json/amF0XHEa.json", encoding="utf-8") as partida:
    partida1 = json.load(partida)   
print(partida1)
