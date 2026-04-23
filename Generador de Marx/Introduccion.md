# Sistema de Alimentación para Generador Marx de 13 kV

## 1. Arquitectura General

```mermaid
flowchart LR
A[Fuente 12V CC] --> B[Conmutación ZVS]
B --> C[Transformación Flyback]
C --> D[Rectificación HV]
D --> E[Carga del Generador Marx]
E --> F[Pulso de Salida ≈13kV]
```

---

## 2. Descripción por Etapas

### 2.1 Fuente Primaria de Energía (12V CC)

| Parámetro | Valor típico |
|---|---|
| Tensión nominal | 12 V |
| Corriente recomendada | 5 A – 15 A |

**Función:** suministrar potencia de entrada al sistema.

---

### 2.2 Etapa de Conmutación ZVS

| Parámetro | Valor típico |
|---|---|
| Topología | Resonante |
| Frecuencia | 20 kHz – 60 kHz |
| Dispositivos | MOSFETs |

**Función:** convertir corriente continua en señal de alta frecuencia para excitar el transformador.

---

### 2.3 Etapa Elevadora Flyback

| Parámetro | Descripción |
|---|---|
| Núcleo | Ferrita |
| Relación de espiras | Alta |
| Salida | Alta tensión pulsante |

**Función:** elevar el nivel de tensión mediante acoplamiento magnético.

---

### 2.4 Rectificación de Alta Tensión

| Elemento | Función |
|---|---|
| Diodo HV | Rectificación |
| Capacitor HV | Filtrado opcional |

**Salida estimada:** 1 kV a 3 kV CC.

---

### 2.5 Etapa de Carga del Generador Marx

- Resistencias limitadoras de corriente  
- Capacitores por etapa  
- Carga en paralelo  
- Descarga en serie

---

### 2.6 Salida Pulsada

| Parámetro | Valor |
|---|---|
| Voltaje pico estimado | ≈13 kV |
| Duración | Corta |
| Naturaleza | Impulso |

---

## 3. Consideraciones de Seguridad

- Descarga manual de capacitores antes de intervenir.  
- Distancias de aislamiento adecuadas.  
- Uso de guantes y herramientas aisladas.  
- Operación supervisada.

---

## 4. Observaciones

El rendimiento final depende de pérdidas en conmutación, aislamiento, calidad del flyback y diseño del banco Marx.
```