import numpy as np
import matplotlib.pyplot as plt

""" Modelo de Harrison.

Aplicación:
    Modelo comparativo cuando EF > 1 y Pwf' puede tomar valores negativos.

Limitaciones:
    Debe validarse contra datos reales y contra la fuente técnica específica
    usada. No sustituye simulación ni pruebas de presión.

Referencia APA:
    Harrison, J. (s. f.). Formulación IPR modificada para eficiencia de flujo.
"""


# VALORES DE PRUEBA
Pb = 2000.0      # psi
Pwf = 500.0      # psi
Pws = 2000.0     # psi
Qo = 200.0       # STB/d
EF = 2.0         # adimensional

# MODELO DE HARRISON
def calcular_harrison(presiones, pwf, pws, qo, ef):
    """ Calcula Qomax y la curva IPR de Harrison. """
    if pws <= 0:
        raise ValueError("Pws debe ser mayor que cero.")
    if pwf < 0 or pwf >= pws:
        raise ValueError("Pwf debe ser mayor o igual a cero y menor que Pws.")
    if qo <= 0:
        raise ValueError("Qo debe ser mayor que cero.")
    if ef <= 0:
        raise ValueError("EF debe ser mayor que cero.")

    # Presión corregida por eficiencia de flujo para toda la curva
    pwf_prima = pws - ((pws - presiones) * ef)

    # Presión corregida del dato de prueba
    pwf_prima_dato = pws - ((pws - pwf) * ef)

    # Denominador de Harrison
    denominador = 1.2 - (0.2 * np.exp(1.792 * (pwf_prima_dato / pws)))

    if denominador <= 0:
        raise ValueError("El denominador de Harrison no es válido.")

    # Gasto máximo Qomax = Qo / [1.2 - 0.2 exp(1.792(Pwf'_dato / Pws))]
    qomax = qo / denominador

    # Curva Harrison Qo = Qomax [1.2 - 0.2 exp(1.792(Pwf' / Pws))]
    gastos = qomax * (
        1.2 - (0.2 * np.exp(1.792 * (pwf_prima / pws)))
    )

    return qomax, gastos, pwf_prima

# CÁLCULO
presiones = np.linspace(0, Pws, 100)

qomax, gastos, PwfPrima = calcular_harrison(
    presiones=presiones,
    pwf=Pwf,
    pws=Pws,
    qo=Qo,
    ef=EF
)

# RESULTADOS
print("Modelo de Harrison")
print(f"EF = {EF:.2f}")
print(f"Qomax = {qomax:.2f} STB/d")
print(f"Pwf' mínimo = {np.min(PwfPrima):.2f} psi")

# GRÁFICA
plt.figure(figsize=(8, 5))

plt.plot(
    gastos,
    presiones,
    linewidth=2,
    label=f"Harrison, EF = {EF:.2f}"
)

plt.scatter(
    Qo,
    Pwf,
    marker="o",
    label="Dato de prueba"
)

plt.title("Curva IPR | Modelo de Harrison")
plt.xlabel("Gasto de aceite, Qo (STB/d)")
plt.ylabel("Presión, Pwf (psi)")

plt.xlim(0, max(np.nanmax(gastos), Qo) * 1.10)
plt.ylim(0, Pws)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()