#Referencia: https://www.freecodecamp.org/portuguese/news/nova-linha-em-python-e-como-usar-print-em-python-sem-uma-nova-linha/
#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
def valor_json():
    with open('Arquivos_Json/amF0XHEa.json', encoding="utf-8") as partida:
        partida1 = json.load(partida)
        return partida1   
dados_manipulavel = valor_json()

estadio = dados_manipulavel["copa-do-brasil"][0]["estadio"]["nome_popular"]
placar = dados_manipulavel["copa-do-brasil"][0]["placar"]
status = dados_manipulavel["copa-do-brasil"][0]["status"]
print('Estádio: ', estadio, "\nPlacar: ", placar,"\nStatus: ",status)
