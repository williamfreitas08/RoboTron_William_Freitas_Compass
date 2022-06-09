#Referencia: https://www.freecodecamp.org/portuguese/news/nova-linha-em-python-e-como-usar-print-em-python-sem-uma-nova-linha/
#Importa a biblioteca JSON do Python
import json

#Função que recebe caminho do arquivo JSON e armazena na variável partida
def valor_json():
    with open('d:\Desktop\RoboTron_William_Freitas_Compass\Exercicio Dia 7/json/amF0XHEa.json', encoding="utf-8") as partida:
        partida1 = json.load(partida)
        return partida1   
dados_manipulavel = valor_json()

placar_mandante = dados_manipulavel["copa-do-brasil"]["placar_mandante"]

placar_visitante = dados_manipulavel["copa-do-brasil"][0]["placar_visitante"]

if  placar_mandante > placar_visitante:
    time_vencedor = dados_manipulavel["copa-do-brasil"][0]["time_mandante"]["nome_popular"]
    print("O time que Venceu foi : {}".format(time_vencedor))

elif placar_mandante < placar_visitante:
    time_vencedor = dados_manipulavel["copa-do-brasil"][0]["time_visitante"]["nome_popular"]
    print("O time que Venceu foi : {}".format(time_vencedor))

else:
    print("O jogo terminou empatado!")
  


