# PEM-Alexander
Descripciones para PEM en donde podemos ver muchas cosas con respecto a muchas cosas


# 🧪 Cálculo de Cantidad de Sulfato de Cobre para una Resistencia Deseada

Este script en Python permite calcular la cantidad de **sulfato de cobre (CuSO₄)** necesaria para preparar una solución con una resistencia eléctrica específica, en función del área transversal del conductor de líquido.

## ✅ Entradas

- `R_objetivo`: Resistencia requerida (en ohmios, Ω)
- `area_m2`: Área transversal del canal o tubo por donde pasa la solución (en metros cuadrados, m²)

## 📤 Salidas

- `longitud_m`: Longitud necesaria del líquido (en m), asumiendo tubo cuadrado
- `volumen_m3`: Volumen de la solución (en metros cúbicos)
- `volumen_L`: Volumen de la solución (en litros)
- `resistividad_ohm_m`: Resistividad necesaria del líquido (en ohm·metro)
- `concentracion_gL`: Concentración estimada de CuSO₄ necesaria (en gramos por litro)
- `masa_CuSO4_g`: Masa total de CuSO₄ necesaria (en gramos)

## 📐 Supuestos

- El canal por donde pasa la corriente es **cuadrado**, por lo tanto:

  \[
  \text{longitud} = \sqrt{\text{área}}
  \]

- Se usa una relación empírica basada en datos experimentales del sulfato de cobre:

  \[
  \rho_{\text{cm}} = 100 \cdot C^{-0.85}
  \]

  Donde:
  - \( \rho_{\text{cm}} \): Resistividad en ohm·centímetro
  - \( C \): Concentración en g/L
