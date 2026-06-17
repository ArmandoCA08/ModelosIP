import numpy as np
import matplotlib.pyplot as plt

""" Modelo de Moore / IPR lineal.

Aplicación:
    Pozos de aceite bajosaturado con flujo monofásico, cuando Pwf > Pb.

Limitaciones:
    No representa flujo bifásico aceite-gas, no considera daño, estimulación
    ni variación de propiedades PVT.

Referencia APA:
    Beggs, H. D. (2003). Production Optimization Using NODAL Analysis.
    OGCI and Petroskills Publications.
"""

# VALORES DE PRUEBA
Pb = 2000.0      # psi
Pwf = 500.0      # psi
Pws = 2000.0     # psi
Qo = 200.0       # STB/d
EF = 2.0         # adimensional, no se usa en Moore

# MODELO DE MOORE
def calcular_moore(presiones, pwf, pws, qo):
    """Calcula el índice de productividad, Qomax y la curva IPR lineal."""
    if pws <= 0:
        raise ValueError("Pws debe ser mayor que cero.")
    if pwf < 0 or pwf >= pws:
        raise ValueError("Pwf debe ser mayor o igual a cero y menor que Pws.")
    if qo <= 0:
        raise ValueError("Qo debe ser mayor que cero.")

    # Índice de productividad: J = Qo / (Pws - Pwf)
    j = qo / (pws - pwf)

    # Gasto máximo cuando Pwf = 0
    qomax = j * pws

    # Curva IPR lineal: q = J(Pws - P)
    gastos = j * (pws - presiones)

    return j, qomax, gastos

# CÁLCULO
presiones = np.linspace(0, Pws, 100)
J, qomax, gastos = calcular_moore(presiones, Pwf, Pws, Qo)

print("Modelo de Moore")
print(f"J     = {J:.4f} STB/d/psi")
print(f"Qomax  = {qomax:.2f} STB/d")

# GRÁFICA
plt.figure(figsize=(8, 5))
plt.plot(gastos, presiones, linewidth=2, label="Moore")
plt.scatter(Qo, Pwf, marker="o", label="Dato de prueba")

plt.title("Curva IPR | Modelo de Moore")
plt.xlabel("Gasto de aceite, Qo (STB/d)")
plt.ylabel("Presión, Pwf (psi)")
plt.xlim(0, qomax * 1.10)
plt.ylim(0, Pws)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
