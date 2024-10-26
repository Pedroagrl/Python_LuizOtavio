velocidade = 61
local_carro = 100

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RANDAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RANDAR_RANGE) and local_carro <= (LOCAL_1 + RANDAR_RANGE) and \
    vel_carro_pass_radar_1

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print("Carro pasou o radar 1")

if carro_multado_radar_1:
    print('Carro multado em radar 1')