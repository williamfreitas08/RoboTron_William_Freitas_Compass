#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
def valor_json():
    with open('Arquivos_Json/amF0XHEa.json',encoding="utf-8") as partida:
        partida1 = json.load(partida)
        return partida1   
dados_manipulavel = valor_json()

print(dados_manipulavel)

for time_valor in dados_manipulavel:
   print(time_valor)
print(dados_manipulavel["copa-do-brasil"][0]["time_visitante"])



