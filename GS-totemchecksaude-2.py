import random

def printa_dicionarios(dicionario):
    for key in dicionario.keys():
        if type(dicionario[key]) is dict:
            printa_dicionarios(dicionario[key])
        else:
            print(f"{key} : {dicionario[key]}")
    return

# Não implementei a função, pois necessita de IA e o tempo não permitiria, mas no futuro ele pegará o CPF por voz e tirará foto para analisar a pupila e palidez.
# Possíveis respostas dos sensores
poss_temp = [33, 34, 35, 36, 37, 38, 39, 40]
poss_press_sis = [125, 128, 129, 150, 156, 160, 165, 168]
poss_press_dia = [80, 82, 85, 87, 90, 95, 100, 110, 120]
poss_s_ou_n = ["sim", "não"]

# A fim de demonstração, vou randomizar eles para apresentar um resultado.
sintomas = {
    "fala_alterada": random.choice(poss_s_ou_n),
    "temperatura": random.choice(poss_temp),
    "pressao_sis": random.choice(poss_press_sis),
    "pressao_dia": random.choice(poss_press_dia),
    "palidez": random.choice(poss_s_ou_n),
    "pupila_dilatada": random.choice(poss_s_ou_n),
}
printa_dicionarios(sintomas)

# Essa variável vai somando o grau de gravidade conforme os sintomas que a pessoa apresentará.
gravidade = 0

if sintomas["fala_alterada"] == "sim":
    gravidade += 3
if sintomas["temperatura"] < 35 or sintomas["temperatura"] > 38:
    gravidade += 3
if sintomas["pressao_sis"] < 129 or sintomas["pressao_sis"] > 160:
    gravidade += 3
if sintomas["pressao_dia"] < 84 or sintomas["pressao_dia"] > 100:
    gravidade += 3
if sintomas["palidez"] == "sim":
    gravidade += 3
if sintomas["pupila_dilatada"] == "sim":
    gravidade += 3

# Aqui são as filas por pulseiras, priorizando a ordem de atendimento.
atendimento = {
    "fila_azul" : ["Maria","Roberta"],
    "fila_verde" : ["Anahi","Miguel"],
    "fila_amarelo" : ["Cristian","Harry"],
    "fila_laranja" : ["Rouge","Diego"],
    "fila_vermelho" : ["Velhos","Danilo"]
}

# Colocando a paciente na fila, de acordo com sua pulseira.
if gravidade == 3:
    atendimento["fila_azul"].append(nome)
    print("Pulseira Azul")
if gravidade == 6:
    atendimento["fila_verde"].append(nome)
    print("Pulseira Verde")
if gravidade == 9:
    atendimento["fila_amarelo"].append(nome)
    print("Pulseira Amarela")
if gravidade == 12:
    atendimento["fila_laranja"].append(nome)
    print("Pulseira Laranja")
if gravidade == 15:
    atendimento["fila_vermelho"].append(nome)
    print("Pulseira Vermelha")

# Tornando a fila em uma só
ordem_atendimento = atendimento["fila_vermelho"] + atendimento["fila_laranja"] + atendimento["fila_amarelo"] + atendimento["fila_verde"] + atendimento["fila_azul"]

print(ordem_atendimento)