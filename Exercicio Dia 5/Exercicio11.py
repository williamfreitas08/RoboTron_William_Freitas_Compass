# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, 
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração 
# mínima de 1 hora e máxima de 24 horas. Entrada: A entrada contém dois valores 
# inteiros representando a hora de início e a hora de fim do jogo. Saída: Apresente 
# a duração do jogo conforme exemplo abaixo.



inicio_jogo = int(input("Digite a Hora de Início do JOGO: "))

final_jogo = int(input("Digite a Hora do Fim do JOGO : "))

hora = 0

if (inicio_jogo >= final_jogo):
    print(f"O JOGO DUROU {hora} HORA(S)", (24-inicio_jogo)+final_jogo)
else:
    print(f"O JOGO DUROU {hora} HORA(S)", final_jogo-inicio_jogo)