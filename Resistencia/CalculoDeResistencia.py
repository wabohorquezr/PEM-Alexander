import math

def calcular_cu_so4(R_objetivo, area_m2):
    # Longitud del cuadrado
    lado_m = math.sqrt(area_m2)
    longitud_m = lado_m  # lado = longitud porque es un tubo cuadrado
    
    # Cálculo de la resistividad necesaria
    rho_m = R_objetivo * (area_m2 / longitud_m)
    
    # Convertimos a ohm.cm para usar la curva empírica
    rho_cm = rho_m * 100  # 1 Ω·m = 100 Ω·cm
    
    # Invertimos la relación empírica para encontrar concentración (g/L)
    # Aproximación basada en gráfica: rho = 100 * C^(-0.85)
    concentracion_gL = (100 / rho_cm) ** (1 / 0.85)

    # Volumen del líquido en m³ y litros
    volumen_m3 = area_m2 * longitud_m
    volumen_L = volumen_m3 * 1000  # 1 m³ = 1000 litros

    # Masa de CuSO4 necesaria
    masa_g = concentracion_gL * volumen_L

    # Resultados
    return {
        "longitud_m": longitud_m,
        "volumen_m3": volumen_m3,
        "volumen_L": volumen_L,
        "resistividad_ohm_m": rho_m,
        "concentracion_gL": concentracion_gL,
        "masa_CuSO4_g": masa_g
    }

# Ejemplo de uso:

R = int(input("Introdusca el valor buscado en la resistencia Ohmica necesaria:  "))
A = float(input("Introdusca el area transversal:  "))
resultados = calcular_cu_so4(R ,A)

print(resultados)
