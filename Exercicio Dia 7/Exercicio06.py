#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
def valor_json():
    with open('Arquivos_Json/GxdV3pRP.json',encoding="utf-8") as campeonato:
        campeonato1 = json.load(campeonato)
        return campeonato1   
dados_campeonato= valor_json()

print(dados_campeonato["edicao_atual"])
print(dados_campeonato["fase_atual"])
print(dados_campeonato["rodada_atual"])


