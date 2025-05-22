# PEM-Alexander
Descripciones para PEM en donde podemos ver muchas cosas con respecto a muchas cosas


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

\begin{itemize}
  \item \( R \): resistencia total \([ \Omega ]\)
  \item \( \rho \): resistividad del material \([ \Omega \cdot \text{m} ]\)
  \item \( l \): longitud del conductor \([ \text{m} ]\)
  \item \( A \): área transversal del conductor \([ \text{m}^2 ]\)
\end{itemize}


---

## 🧮 Supuestos geométricos

Para hacer una estimación práctica, se asume lo siguiente:

- Longitud del líquido conductor:  
  \[
  l = 0.1 \, \text{m} \quad \text{(10 cm)}
  \]
  
- Área transversal:  
  \[
  A = 1 \, \text{cm}^2 = 1 \times 10^{-4} \, \text{m}^2
  \]

---

## 🔄 Cálculo de resistividad requerida

Reordenando la fórmula para obtener la resistividad específica:

\[
\rho = R \cdot \frac{A}{l} = 50 \cdot \frac{1 \times 10^{-4}}{0.1} = 0.05 \, \Omega\cdot\text{m}
\]

Convertimos a Ω·cm (multiplicamos por 100):

\[
\rho = 0.05 \, \Omega\cdot\text{m} = 5 \, \Omega\cdot\text{cm}
\]

---

## 📊 Interpretación usando la gráfica

Al observar el valor de **5 Ω·cm** en el eje vertical de la gráfica de CuSO₄, se estima:

- La concentración correspondiente es de aproximadamente **85 g/L**

---

## ✅ Resultado estimado

> Para obtener una resistencia de **50 Ω** en una celda de **10 cm de largo** y **1 cm² de sección transversal**, se requiere una **solución de sulfato de cobre con concentración aproximada de 85 g/L**.

---

## 🧪 Nota adicional

Este valor puede refinarse si se usan otras dimensiones (longitud y área). El cálculo es adaptable a otros casos usando la misma lógica.

