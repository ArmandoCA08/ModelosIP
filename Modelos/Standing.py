import numpy as np
import matplotlib.pyplot as plt

"""
Modelo de Standing.

Aplicación:
    Pozos de aceite con flujo bifásico donde se desea considerar eficiencia
    de flujo. EF < 1 indica daño; EF = 1 pozo ideal; EF > 1 estimulación.

Limitaciones:
    Depende de una EF confiable. No sustituye pruebas de presión ni análisis
    detallado de daño.

Referencias APA:
    Standing, M. B. (1970). Inflow performance relationships for damaged wells
    producing by solution-gas drive. Journal of Petroleum Technology, 22(11),
    1399-1400. https://doi.org/10.2118/3237-PA

    Vogel, J. V. (1968). Inflow performance relationships for solution-gas
    drive wells. Journal of Petroleum Technology, 20(1), 83-92.
    https://doi.org/10.2118/1476-PA
"""

# VALORES DE PRUEBA
Pb = 2000.0      # psi
Pwf = 500.0      # psi
Pws = 2000.0     # psi
Qo = 200.0       # STB/d
EF = 2.0         # adimensional

# MODELO DE STANDING
def calcular_standing(presiones, pwf, pws, qo, ef):
    """Calcula qmax y la curva IPR de Standing."""
    if pws <= 0:
        raise ValueError("Pws debe ser mayor que cero.")
    if pwf < 0 or pwf >= pws:
        raise ValueError("Pwf debe ser mayor o igual a cero y menor que Pws.")
    if qo <= 0:
        raise ValueError("Qo debe ser mayor que cero.")
    if ef <= 0:
        raise ValueError("EF debe ser mayor que cero.")

    # Presión corregida por eficiencia de flujo
    pwf_prima = pws - ((pws - presiones) * ef)

    # qmax se estima con el dato de prueba usando la base de Vogel
    relacion_dato = pwf / pws
    denominador = 1 - 0.2 * relacion_dato - 0.8 * relacion_dato**2
    if denominador <= 0:
        raise ValueError("El denominador de Standing no es válido.")

    qomax = qo / denominador

    # Curva Standing con Pwf'
    relacion_curva = pwf_prima / pws
    gastos = qomax * (1 - 0.2 * relacion_curva - 0.8 * relacion_curva**2)

    return qomax, gastos, pwf_prima

# CÁLCULO
presiones = np.linspace(0, Pws, 100)
qomax, gastos, PwfPrima = calcular_standing(presiones, Pwf, Pws, Qo, EF)

print("Modelo de Standing")
print(f"EF    = {EF:.2f}")
print(f"Qomax  = {qomax:.2f} STB/d")
print(f"Pwf' mínimo = {np.min(PwfPrima):.2f} psi")


# GRÁFICA
plt.figure(figsize=(8, 5))
plt.plot(gastos, presiones, linewidth=2, label=f"Standing, EF = {EF:.2f}")
plt.scatter(Qo, Pwf, marker="o", label="Dato de prueba")

plt.title("Curva IP | Modelo de Standing")
plt.xlabel("Gasto de aceite, Qo (STB/d)")
plt.ylabel("Presión, Pwf (psi)")
plt.xlim(0, max(np.nanmax(gastos), Qo) * 1.10)
plt.ylim(0, Pws)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
