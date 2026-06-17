import numpy as np
import matplotlib.pyplot as plt

""" Modelo de Vogel.

Aplicación:
    Pozos de aceite saturado con flujo bifásico aceite-gas.

Limitaciones:
    Correlación empírica para yacimientos con empuje por gas en solución.
    No considera daño ni estimulación de forma explícita.

Referencia APA:
    Vogel, J. V. (1968). Inflow performance relationships for solution-gas
    drive wells. Journal of Petroleum Technology, 20(1), 83-92.
    https://doi.org/10.2118/1476-PA
"""

# VALORES DE PRUEBA
Pb = 2000.0      # psi
Pwf = 500.0      # psi
Pws = 2000.0     # psi
Qo = 200.0       # STB/d
EF = 2.0         # adimensional, no se usa en Vogel clásico

# MODELO DE VOGEL
def calcular_vogel(presiones, pwf, pws, qo):
    """ Calcula qmax y la curva IPR de Vogel. """
    if pws <= 0:
        raise ValueError("Pws debe ser mayor que cero.")
    if pwf < 0 or pwf >= pws:
        raise ValueError("Pwf debe ser mayor o igual a cero y menor que Pws.")
    if qo <= 0:
        raise ValueError("Qo debe ser mayor que cero.")

    # Relación de presión del dato de prueba
    relacion_dato = pwf / pws

    # Denominador de Vogel
    denominador = 1 - 0.2 * relacion_dato - 0.8 * relacion_dato**2
    if denominador <= 0:
        raise ValueError("El denominador de Vogel no es válido.")

    # Gasto máximo teórico
    qomax = qo / denominador

    # Curva IPR de Vogel
    relacion_curva = presiones / pws
    gastos = qomax * (1 - 0.2 * relacion_curva - 0.8 * relacion_curva**2)

    return qomax, gastos

# CÁLCULO
presiones = np.linspace(0, Pws, 100)
qomax, gastos = calcular_vogel(presiones, Pwf, Pws, Qo)

print("Modelo de Vogel")
print(f"Qomax = {qomax:.2f} STB/d")

# GRÁFICA
plt.figure(figsize=(8, 5))
plt.plot(gastos, presiones, linewidth=2, label="Vogel")
plt.scatter(Qo, Pwf, marker="o", label="Dato de prueba")

plt.title("Curva IPR | Modelo de Vogel")
plt.xlabel("Gasto de aceite, Qo (STB/d)")
plt.ylabel("Presión, Pwf (psi)")
plt.xlim(0, qomax * 1.10)
plt.ylim(0, Pws)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()