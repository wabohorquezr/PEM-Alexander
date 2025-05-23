
# 📘 Cálculo de Concentración de Sulfato de Cobre (CuSO₄) para Obtener una Resistencia de 50 Ω

## 🧾 Objetivo

Queremos determinar  la concentración necesaria de una solución de sulfato de cobre (CuSO₄) que produzca una **resistencia total de 50 ohmios**, en este caso resistividad específica en función de la concentración la tomamos de ejmplo por meido de la imagen.[Pagina de la imagen](http://www.kronjaeger.com/hv/hv/comp/res/index.html)


![Imagen](http://www.kronjaeger.com/hv/hv/comp/res/spezres.png)

---

## 📉 Información de la Gráfica

- **Eje vertical**: Resistividad específica (ρ) en **Ω·cm**
- **Eje horizontal**: Concentración de CuSO₄ en **g/L**
- La curva muestra que al aumentar la concentración, la resistividad disminuye.
- El rango de resistividad está entre **1 y 1000 Ω·cm**

---

## 📐 Fundamento teórico

La resistencia total de un conductor está dada por:

$R = \rho \cdot \frac{l}{A}$


Donde:

- $R$: resistencia total $[\Omega]$
- $\rho$: resistividad del material $[\Omega \cdot \text{m}]$
- $l$: longitud del conductor $[\text{m}]$
- $A$: área transversal del conductor $[\text{m}^2]$


---

## 🧮 Supuestos geométricos

Para hacer una estimación práctica, se asume lo siguiente:

- Longitud del líquido conductor:  
  $l = 0.1 \, \text{m} \quad \text{(10 cm)}$
  
- Área transversal:  
  $A = 1 \, \text{cm}^2 = 1 \times 10^{-4} \, \text{m}^2$

---

## 🔄 Cálculo de resistividad requerida

Reordenando la fórmula para obtener la resistividad específica:

$\rho = R \cdot \frac{A}{l} = 50 \cdot \frac{1 \times 10^{-4}}{0.1} = 0.05 \, \Omega\cdot\text{m}$

Convertimos a Ω·cm (multiplicamos por 100):

$\rho = 0.05 \, \Omega\cdot\text{m} = 5 \, \Omega\cdot\text{cm}$

---

## 📊 Interpretación usando la gráfica

Al observar el valor de **5 Ω·cm** en el eje vertical de la gráfica de CuSO₄, se estima:

- La concentración correspondiente es de aproximadamente **85 g/L**

Logrado por medio de la elavoracion del codigo:

```python
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

```
---


## Creacion de la soluccion de cobre 

En la creacion de la solucion de cobre mi gui en funcion al video [How to Prepare a Standard Solution of Copper(II) Sulfate](http://youtube.com/watch?v=PJ_kgmJykUM)

En funcion a lo encontrado por medio de el video obtenemos 

[Solucion liquida con sulfato de cobre](https://www.youtube.com/shorts/1H3qh7PhQ4s)

[Resistencia de agua(Carcasa)](https://www.youtube.com/shorts/2VBhNsMEiJs)

---

## ✅ Resultado estimado

> Para obtener una resistencia de **50 Ω** en una celda de **10 cm de largo** y **1 cm² de sección transversal**, se requiere una **solución de sulfato de cobre con concentración aproximada de 85 g/L**.

---

## 🧪 Nota adicional

Este valor puede refinarse si se usan otras dimensiones (longitud y área). El cálculo es adaptable a otros casos usando la misma lógica.




![Solucion](Solucion.md)