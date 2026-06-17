import numpy as np
import matplotlib.pyplot as plt

""" Modelo de Vogel Generalizado.

Aplicación:
    Tramo combinado: comportamiento lineal arriba de Pb y comportamiento tipo
    Vogel debajo de Pb.

Limitaciones:
    Requiere Pb confiable. Si Pb = Pws, qPb = 0. Debe validarse con datos de
    prueba y no extrapolarse sin criterio.

Referencias APA:
    Vogel, J. V. (1968). Inflow performance relationships for solution-gas
    drive wells. Journal of Petroleum Technology, 20(1), 83-92.
    https://doi.org/10.2118/1476-PA

    Patton, L. D., & Goland, L. (1976). Generalized IPR curves for solution
    gas-drive reservoirs. Society of Petroleum Engineers.
"""

# VALORES DE PRUEBA
Pb = 2000.0      # psi
Pwf = 500.0      # psi
Pws = 2000.0     # psi
Qo = 200.0       # STB/d
EF = 2.0         # adimensional, no se usa en esta formulación

# MODELO DE VOGEL GENERALIZADO
def calcular_vogel_generalizado(pb, pwf, pws, qo, puntos=100):
    """ Calcula qPb, curva de gastos y presiones del tramo menor o igual a Pb. """
    if pb <= 0:
        raise ValueError("Pb debe ser mayor que cero.")
    if pws <= 0:
        raise ValueError("Pws debe ser mayor que cero.")
    if pwf < 0 or pwf >= pws:
        raise ValueError("Pwf debe ser mayor o igual a cero y menor que Pws.")
    if pb > pws:
        raise ValueError("Pb no debería ser mayor que Pws.")
    if qo <= 0:
        raise ValueError("Qo debe ser mayor que cero.")

    # Índice de productividad calculado con el dato de prueba
    j = qo / (pws - pwf)

    # Vector de presiones de 0 a Pb
    presiones_pb = np.linspace(0, pb, puntos)

    # Gasto a la presión de burbuja
    gasto_burbuja = j * (pws - pb)

    # Tramo bajo Pb con forma de Vogel
    relacion_pb = presiones_pb / pb
    gastos = gasto_burbuja + (((j * pb) / 1.8) * (1 - 0.2 * relacion_pb - 0.8 * relacion_pb**2))

    return j, gasto_burbuja, gastos, presiones_pb

# CÁLCULO
J, qPb, gastos, presiones_pb = calcular_vogel_generalizado(Pb, Pwf, Pws, Qo)

print("Modelo de Vogel generalizado")
print(f"J    = {J:.4f} STB/d/psi")
print(f"qPb  = {qPb:.2f} STB/d")
print(f"qmax aproximado = {np.max(gastos):.2f} STB/d")

# GRÁFICA
plt.figure(figsize=(8, 5))
plt.plot(gastos, presiones_pb, linewidth=2, label="Vogel generalizado")
plt.scatter(Qo, Pwf, marker="o", label="Dato de prueba")

plt.title("Curva IPR | Modelo Vogel Generalizado")
plt.xlabel("Gasto de aceite, Qo (STB/d)")
plt.ylabel("Presión, Pwf (psi)")
plt.xlim(0, max(np.nanmax(gastos), Qo) * 1.10)
plt.ylim(0, Pws)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()