import math

# Entrada de dados
pos0 = float(input("Posição inicial (m): "))
h_f = float(input("Altura final (m): "))
vel_0 = float(input("Velocidade inicial (m/s): "))
angl0 = float(input("Ângulo de lançamento (graus): "))
inst_t = float(input("Instante de tempo (s): "))

# Conversão de ângulo para radianos
inst_t = math.radians(angl0)

# Constante da gravidade
g = 9.81

# Cálculo das velocidades iniciais
vel_0x = vel_0 * math.cos(angl0)
vel_0y = vel_0 * math.sin(angl0)

# Tempo de queda
t = (vel_0y + math.sqrt(vel_0y**2 + 2 * g * (h_f - pos0))) / g

# Tempo no ar
td1 = vel_0 * math.cos (angl0) / g

# Alcance horizontal
xm = vel_0x * t

# Altura máxima
hmax = (vel_0y ** 2) / (2 * g)

# Velocidade na altura máxima
v_hmax = math.sqrt(vel_0x**2 + (vel_0y - g ** t)**2)

# Velocidade no ponto de chegada (y = 0)
vx_cheg = vel_0x
vy_cheg = vel_0y - g * t
v_cheg = math.sqrt(vx_cheg**2 + vy_cheg**2)

# Coordenadas no instante 
inst_tx = vel_0x * inst_t
inst_ty = pos0 + vel_0y * inst_t - 0.5 * g * inst_t**2

# Velocidade no instante 
vel_inst_x = vel_0x
vel_inst_y = vel_0y - g * inst_t
vel_inst = math.sqrt(vel_inst_x**2 + vel_inst_y**2)

# Saída de dados
print("Velocidade inicial na direção x (vel_0x):", vel_0x, "m/s")
print("Velocidade inicial na direção y (vel_0y):", vel_0y, "m/s")
print("Tempo de queda (t):", t, "s")
print("Alcance horizontal (xm):", xm, "m")
print("Altura máxima (hmax):", hmax, "m")
print("Velocidade na posição hmax (vx_hmax, vy_hmax, v_hmax):", vel_0x, "m/s,", vel_0y - g * t, "m/s,", v_hmax, "m/s")
print("Velocidade no ponto de chegada (vx_cheg, vy_cheg, v_cheg):", vx_cheg, "m/s,", vy_cheg, "m/s,", v_cheg, "m/s")
print("Coordenadas no instante td (inst_tx, inst_ty):", inst_tx, ",", inst_ty, "m")
print("Velocidade no instante td (vel_inst_x, vel_inst_y, vel_inst):", vel_inst_x, "m/s,", vel_inst_y, "m/s,", vel_inst, "m/s")
