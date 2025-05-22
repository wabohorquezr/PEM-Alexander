import math

def estimar_concentracion_cuSO4(resistencia_ohm_cm):
    """
    Estima la concentración de CuSO4 en g/L a partir de la resistencia específica en Ohm·cm,
    usando una aproximación logarítmica basada en la gráfica.
    """
    # Datos aproximados extraídos visualmente de la gráfica:
    # (concentración g/L, resistencia específica Ohm·cm)
    datos = [
        (2, 160),
        (4, 90),
        (6, 50),
        (10, 30),
        (20, 15),
        (40, 8)
    ]
    
    # Convertir a log-log para interpolación logarítmica
    log_c = [math.log10(c) for c, r in datos]
    log_r = [math.log10(r) for c, r in datos]

    # Interpolación lineal en log-log
    log_res = math.log10(resistencia_ohm_cm)
    for i in range(len(log_r) - 1):
        if log_r[i] >= log_res >= log_r[i+1]:
            # Interpolamos log(concentración)
            m = (log_c[i+1] - log_c[i]) / (log_r[i+1] - log_r[i])
            log_conc = log_c[i] + m * (log_res - log_r[i])
            return 10**log_conc

    raise ValueError("Resistencia fuera del rango de interpolación (8–160 Ohm·cm)")

def calcular_sulfato_y_agua(resistencia_deseada, largo_cm, ancho_cm, alto_cm):
    volumen_cm3 = largo_cm * ancho_cm * alto_cm
    volumen_L = volumen_cm3 / 1000  # 1 L = 1000 cm³

    concentracion = estimar_concentracion_cuSO4(resistencia_deseada)
    masa_sulfato = concentracion * volumen_L

    return masa_sulfato, volumen_L

# ===== EJEMPLO DE USO =====

# Entradas
resistencia_deseada = 50       # Ohm·cm
largo_cm = 11
ancho_cm = 5
alto_cm = 3

# Cálculo


largo = float(input("Dimensiones del liquido "))
ancho = float(input("Dimensiones del liquido "))
alto = float(input("Dimensiones del liquido "))



resistencia = float(input("Resistencia Requerida: "))

masa_sulfato, volumen_agua = calcular_sulfato_y_agua(resistencia, largo, ancho, alto)

print(f"Para obtener {resistencia} Ω·cm en una caja de {largo}×{ancho}×{alto} cm:")
print(f"- Sulfato de cobre necesario: {masa_sulfato:.2f} g")
print(f"- Agua destilada: {volumen_agua:.3f} L")
