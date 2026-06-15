# Modelos IPR

Esta carpeta contiene los modelos matemáticos utilizados para construir curvas de comportamiento de afluencia de pozos petroleros, conocidas como curvas **IPR** (*Inflow Performance Relationship*).

Una curva IPR representa la relación entre el gasto de producción del pozo y la presión de fondo fluyente. Es una herramienta de ingeniería de producción utilizada para evaluar el desempeño del pozo bajo diferentes condiciones de abatimiento de presión.

Los modelos considerados inicialmente son:

* Moore
* Vogel
* Standing
* Harrison
* Vogel generalizado

---

## Variables generales

| Símbolo       | Variable                        | Unidades campo | Unidades métricas |
| ------------- | ------------------------------- | -------------: | ----------------: |
| `q_o`         | Gasto de aceite                 |          STB/d |              m³/d |
| `q_{o,max}`   | Gasto máximo teórico de aceite  |          STB/d |              m³/d |
| `P_ws`         | Presión promedio del yacimiento|            psi | kPa, bar o kg/cm² |
| `P_{wf}`      | Presión de fondo fluyente       |            psi | kPa, bar o kg/cm² |
| `P_b`         | Presión de burbuja              |            psi | kPa, bar o kg/cm² |
| `J`           | Índice de productividad         |      STB/d/psi |          m³/d/kPa |
| `EF`          | Eficiencia de flujo             |   adimensional |      adimensional |
| `S`           | Daño o skin                     |   adimensional |      adimensional |
| `a`, `b`, `n` | Coeficientes de ajuste          |   adimensional |      adimensional |

> Nota: las ecuaciones deben manejarse con unidades consistentes. Si se trabaja en sistema inglés, las presiones se usan normalmente en `psi` y los gastos en `STB/d`. Si se trabaja en sistema métrico, se recomienda mantener todas las presiones en una misma unidad y los gastos en `m³/d`.

---

# 1. Modelo de Moore

## Descripción

En este repositorio, el modelo de Moore se considera como una aproximación lineal basada en el índice de productividad. Representa el comportamiento de afluencia cuando el gasto del pozo es proporcional al abatimiento de presión.

## Aplicación

Se aplica principalmente en:

* Pozos de aceite bajosaturado.
* Flujo monofásico.
* Casos donde `P_{wf} > P_b`.
* Análisis inicial de productividad.
* Comparación contra modelos no lineales como Vogel.

## Gasto de aceite

```math
q_o = J(P_r - P_{wf})
```

## Índice de productividad

```math
J = \frac{q_o}{P_ws - P_{wf}}
```

## Gasto de aceite máximo

Cuando `P_{wf} = 0`:

```math
q_{o,max} = J P_ws
```

Sustituyendo el índice de productividad:

```math
q_{o,max} = \frac{q_o P_ws}{P_r - P_{wf}}
```

## Variables

| Símbolo     | Descripción                     | Unidades campo |
| ----------- | ------------------------------- | -------------: |
| `q_o`       | Gasto de aceite medido          |          STB/d |
| `q_{o,max}` | Gasto máximo teórico            |          STB/d |
| `P_ws`      | Presión promedio del yacimiento |            psi |
| `P_{wf}`    | Presión de fondo fluyente       |            psi |
| `J`         | Índice de productividad         |      STB/d/psi |

## Limitaciones

* No representa adecuadamente flujo bifásico aceite-gas.
* No considera liberación de gas en el yacimiento.
* Puede sobreestimar el gasto cuando `P_{wf}` cae por debajo de `P_b`.
* Supone índice de productividad constante.
* No considera daño, estimulación ni variación de propiedades PVT.
* No es recomendable para pozos de gas o pozos con alta complejidad multifásica.

---

# 2. Modelo de Vogel

## Descripción

El modelo de Vogel es una correlación empírica utilizada para representar el comportamiento de afluencia en pozos de aceite con flujo bifásico aceite-gas. Fue desarrollado para yacimientos con empuje por gas en solución.

## Aplicación

Se aplica principalmente en:

* Pozos de aceite saturado.
* Yacimientos con empuje por gas en solución.
* Casos donde `P_{wf} < P_b`.
* Flujo bifásico aceite-gas.
* Construcción de curvas IPR no lineales.

## Gasto de aceite máximo

```math
\frac{q_o}{q_{o,max}} =
1 - 0.2\left(\frac{P_{wf}}{P_ws}\right)
- 0.8\left(\frac{P_{wf}}{P_ws}\right)^2
```

## Gasto a una presión de fondo fluyente

```math
q_o =
q_{o,max}
\left[
1 - 0.2\left(\frac{P_{wf}}{P_ws}\right)
- 0.8\left(\frac{P_{wf}}{P_ws}\right)^2
\right]
```

## Gasto máximo a partir de una prueba de pozo

```math
q_{o,max} =
\frac{q_o}
{
1 - 0.2\left(\frac{P_{wf}}{P_ws}\right)
- 0.8\left(\frac{P_{wf}}{P_ws}\right)^2
}
```

## Variables

| Símbolo     | Descripción                            | Unidades campo |
| ----------- | -------------------------------------- | -------------: |
| `q_o`       | Gasto de aceite a una presión `P_{wf}` |          STB/d |
| `q_{o,max}` | Gasto máximo teórico cuando `P_{wf}=0` |          STB/d |
| `P_ws`      | Presión promedio del yacimiento        |            psi |
| `P_{wf}`    | Presión de fondo fluyente              |            psi |

## Limitaciones

* Es una correlación empírica.
* Fue desarrollada para yacimientos con empuje por gas en solución.
* No considera explícitamente daño de formación.
* No considera estimulación.
* No representa adecuadamente pozos de gas.
* Su aplicación directa puede no ser válida para pozos horizontales, multilaterales o yacimientos altamente heterogéneos.
* Requiere una prueba estabilizada de producción para estimar `q_{o,max}`.
* No debe extrapolarse sin criterio fuera del rango de condiciones para el que fue desarrollada.

---

# 3. Modelo de Standing

## Descripción

El modelo de Standing es una extensión del modelo de Vogel que incorpora la eficiencia de flujo, permitiendo representar pozos dañados o estimulados.

La eficiencia de flujo permite modificar la curva IPR para considerar que el pozo no necesariamente se comporta como un pozo ideal.

## Aplicación

Se aplica principalmente en:

* Pozos de aceite con flujo bifásico.
* Pozos con daño de formación.
* Pozos estimulados.
* Casos donde se desea analizar el efecto de la eficiencia de flujo.
* Comparación entre pozo ideal, dañado y estimulado.


## Eficiencia de flujo

```math
EF = \frac{\Delta P_{ideal}}{\Delta P_{real}}
```

De forma práctica:

```math
EF = \frac{P_ws - P_{wf,ideal}}{P_ws - P_{wf,real}}
```

Interpretación de la eficiencia de flujo:

| Valor de `EF` | Interpretación        |
| ------------: | --------------------- |
|      `EF < 1` | Pozo dañado           |
|      `EF = 1` | Pozo ideal o sin daño |
|      `EF > 1` | Pozo estimulado       |

## Presión de fondo fluyente prima

Una forma práctica de representar el efecto de la eficiencia de flujo es mediante una presión corregida:

```math
P_{wf,c} =
P_r - EF(P_ws - P_{wf})
```

## Relación tipo Vogel corregida

```math
\frac{q_o}{q_{o,max}} =
1 - 0.2\left(\frac{P_{wf,c}}{P_ws}\right)
- 0.8\left(\frac{P_{wf,c}}{P_ws}\right)^2
```

## Gasto estimado

```math
q_o =
q_{o,max}
\left[
1 - 0.2\left(\frac{P_{wf,c}}{P_ws}\right)
- 0.8\left(\frac{P_{wf,c}}{P_ws}\right)^2
\right]
```

## Variables

| Símbolo     | Descripción                         | Unidades campo |
| ----------- | ----------------------------------- | -------------: |
| `q_o`       | Gasto de aceite                     |          STB/d |
| `q_{o,max}` | Gasto máximo teórico                |          STB/d |
| `P_ws`      | Presión promedio del yacimiento     |            psi |
| `P_{wf}`    | Presión de fondo fluyente real      |            psi |
| `P_{wf,c}`  | Presión de fondo fluyente corregida |            psi |
| `EF`        | Eficiencia de flujo                 |   adimensional |

## Limitaciones

* Depende de una estimación confiable de `EF`.
* Mantiene la base empírica del modelo de Vogel.
* No sustituye un análisis de daño mediante pruebas de presión.
* Puede generar resultados no físicos si se usa una eficiencia de flujo muy alta sin control.
* Debe validarse contra datos de prueba de pozo.
* No se recomienda para pozos de gas.
* Su aplicación en pozos horizontales o altamente desviados debe hacerse con precaución.

---

# 4. Modelo de Harrison

## Descripción

El modelo de Harrison se utiliza como una modificación del comportamiento IPR para considerar eficiencia de flujo y evitar ciertos comportamientos no físicos que pueden presentarse al extender directamente el modelo de Vogel o Standing.

## Aplicación

Se aplica principalmente en:

* Pozos de aceite.
* Análisis comparativo de modelos IPR.
* Casos donde se desea evaluar el efecto de la eficiencia de flujo.
* Pozos dañados o estimulados, siempre que se valide la formulación usada.

## Forma general

Una forma práctica de expresar el modelo es mediante una relación modificada de presión normalizada:

```math
\frac{q_o}{q_{o,max}} =
f\left(\frac{P_{wf}}{P_ws}, EF\right)
```

Donde `f` representa una función de ajuste que depende de la presión normalizada y de la eficiencia de flujo.

## Forma polinómica general para implementación

Para fines computacionales, puede representarse como:

```math
\frac{q_o}{q_{o,max}} =
A(EF) +
B(EF)\left(\frac{P_{wf}}{P_ws}\right) +
C(EF)\left(\frac{P_{wf}}{P_ws}\right)^2
```

Por lo tanto:

```math
q_o =
q_{o,max}
\left[
A(EF) +
B(EF)\left(\frac{P_{wf}}{P_ws}\right) +
C(EF)\left(\frac{P_{wf}}{P_ws}\right)^2
\right]
```

> Nota: los coeficientes `A(EF)`, `B(EF)` y `C(EF)` deben definirse con base en la referencia bibliográfica o en la formulación adoptada en el código del repositorio.

## Variables

| Símbolo     | Descripción                                    | Unidades campo |
| ----------- | ---------------------------------------------- | -------------: |
| `q_o`       | Gasto de aceite                                |          STB/d |
| `q_{o,max}` | Gasto máximo teórico                           |          STB/d |
| `P_ws`      | Presión promedio del yacimiento                |            psi |
| `P_{wf}`    | Presión de fondo fluyente                      |            psi |
| `EF`        | Eficiencia de flujo                            |   adimensional |
| `A(EF)`     | Coeficiente dependiente de eficiencia de flujo |   adimensional |
| `B(EF)`     | Coeficiente dependiente de eficiencia de flujo |   adimensional |
| `C(EF)`     | Coeficiente dependiente de eficiencia de flujo |   adimensional |

## Limitaciones

* La ecuación específica debe validarse contra la fuente utilizada.
* Los coeficientes pueden variar según la formulación adoptada.
* Puede no representar correctamente flujo multifásico complejo.
* Requiere comparación contra datos reales de prueba de pozo.
* No sustituye una simulación de yacimientos ni un análisis de pruebas de presión.

---

# 5. Vogel generalizado

## Descripción

El modelo de Vogel generalizado permite extender la forma clásica de Vogel mediante coeficientes de ajuste. Su objetivo es representar distintos comportamientos de afluencia cuando el modelo clásico no ajusta adecuadamente los datos de prueba.

## Aplicación

Se aplica principalmente en:

* Ajuste de curvas IPR a datos reales.
* Comparación contra Vogel clásico.
* Análisis de sensibilidad.
* Estudios académicos o computacionales.
* Casos donde se desea calibrar el comportamiento de afluencia.

## Tipo de pozo recomendado

* Pozos de aceite con datos suficientes de prueba.
* Pozos donde el comportamiento no sea representado adecuadamente por Vogel clásico.
* Casos de análisis comparativo o calibración.

## Ecuación general

```math
\frac{q_o}{q_{o,max}} =
1 - a\left(\frac{P_{wf}}{P_ws}\right)
- b\left(\frac{P_{wf}}{P_ws}\right)^n
```

## Gasto estimado

```math
q_o =
q_{o,max}
\left[
1 - a\left(\frac{P_{wf}}{P_ws}\right)
- b\left(\frac{P_{wf}}{P_ws}\right)^n
\right]
```

## Condición de Vogel clásico

Para recuperar el modelo de Vogel clásico:

```math
a = 0.2
```

```math
b = 0.8
```

```math
n = 2
```

Por lo tanto:

```math
\frac{q_o}{q_{o,max}} =
1 - 0.2\left(\frac{P_{wf}}{P_ws}\right)
- 0.8\left(\frac{P_{wf}}{P_ws}\right)^2
```

## Variables

| Símbolo     | Descripción                     | Unidades campo |
| ----------- | ------------------------------- | -------------: |
| `q_o`       | Gasto de aceite                 |          STB/d |
| `q_{o,max}` | Gasto máximo teórico            |          STB/d |
| `P_ws`      | Presión promedio del yacimiento |            psi |
| `P_{wf}`    | Presión de fondo fluyente       |            psi |
| `a`         | Coeficiente lineal de ajuste    |   adimensional |
| `b`         | Coeficiente no lineal de ajuste |   adimensional |
| `n`         | Exponente de ajuste             |   adimensional |

## Limitaciones

* Requiere calibración con datos reales.
* Los coeficientes `a`, `b` y `n` pueden no tener significado físico directo.
* Puede sobreajustar si se tienen pocos datos de prueba.
* No debe extrapolarse fuera del rango de datos usados para calibrar.
* Debe validarse contra mediciones de campo.
* Su uso sin calibración puede producir curvas no representativas.

---

# Comparación general de aplicación

| Modelo             | Tipo de comportamiento | Tipo de pozo               | Uso principal                     |
| ------------------ | ---------------------- | -------------------------- | --------------------------------- |
| Moore              | Lineal                 | Aceite bajosaturado        | Productividad monofásica          |
| Vogel              | No lineal              | Aceite saturado            | Flujo bifásico aceite-gas         |
| Standing           | No lineal corregido    | Aceite dañado o estimulado | Efecto de eficiencia de flujo     |
| Harrison           | No lineal corregido    | Aceite con ajuste por EF   | Comparación y corrección avanzada |
| Vogel generalizado | No lineal ajustable    | Aceite con datos de prueba | Calibración de curvas IPR         |

---

# Referencias

Vogel, J. V. (1968). *Inflow performance relationships for solution-gas drive wells*. Journal of Petroleum Technology, 20(1), 83–92. https://doi.org/10.2118/1476-PA

Standing, M. B. (1970). *Inflow performance relationships for damaged wells producing by solution-gas drive*. Journal of Petroleum Technology, 22(11), 1399–1400. https://doi.org/10.2118/3237-PA

Standing, M. B. (1971). *Concerning the calculation of inflow performance of wells producing from solution gas drive reservoirs*. Journal of Petroleum Technology, 23(9), 1141–1142.

Lekia, S. D., Evans, R. D., & Evans, R. D. (1990). *Generalized inflow performance relationship for solution-gas drive wells*. Journal of Canadian Petroleum Technology, 29(6). https://doi.org/10.2118/90-06-07

Klins, M. A., & Majcher, M. W. (1992). *Inflow performance relationships for damaged or improved wells producing under solution-gas drive*. Journal of Petroleum Technology, 44(12), 1357–1363. https://doi.org/10.2118/19852-PA

Schlumberger. (s. f.). *Inflow performance relationship*. Energy Glossary. https://glossary.slb.com/terms/i/inflow_performance_relationship


