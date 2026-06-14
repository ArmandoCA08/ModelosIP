# Modelos IPR

Esta carpeta contiene los modelos matemáticos utilizados para construir curvas de comportamiento de afluencia de pozos petroleros, conocidas como curvas **IPR** (*Inflow Performance Relationship*).

Una curva IPR representa la relación entre el gasto de producción del pozo y la presión de fondo fluyente. Es una herramienta de ingeniería de producción utilizada para evaluar el desempeño del pozo bajo diferentes condiciones de abatimiento de presión.

Los modelos considerados inicialmente son:

- Moore
- Vogel
- Standing
- Harrison
- Vogel generalizado

> En futuras versiones se podrán añadir más modelos IPR, siempre que se documenten sus ecuaciones, variables, unidades, supuestos, limitaciones y referencias.

---

## Variables generales

| Símbolo | Variable | Unidades campo | Unidades métricas |
|---|---|---:|---:|
| `q_o` | Gasto de aceite | STB/d | m³/d |
| `q_{o,max}` | Gasto máximo teórico de aceite | STB/d | m³/d |
| `P_r` | Presión promedio del yacimiento | psi | kPa, bar o kg/cm² |
| `P_{wf}` | Presión de fondo fluyente | psi | kPa, bar o kg/cm² |
| `P_b` | Presión de burbuja | psi | kPa, bar o kg/cm² |
| `J` | Índice de productividad | STB/d/psi | m³/d/kPa |
| `EF` | Eficiencia de flujo | adimensional | adimensional |
| `S` | Daño o skin | adimensional | adimensional |
| `a`, `b`, `n` | Coeficientes de ajuste | adimensional | adimensional |

> Nota: las ecuaciones deben manejarse con unidades consistentes. Si se trabaja en sistema inglés, las presiones se usan normalmente en `psi` y los gastos en `STB/d`. Si se trabaja en sistema métrico, se recomienda mantener todas las presiones en una misma unidad y los gastos en `m³/d`.

---

# 1. Modelo de Moore

## Descripción

En este repositorio, el modelo de Moore se considera como una aproximación lineal basada en el índice de productividad. Representa el comportamiento de afluencia cuando el gasto del pozo es proporcional al abatimiento de presión.

Este modelo es equivalente al comportamiento lineal clásico de productividad.

