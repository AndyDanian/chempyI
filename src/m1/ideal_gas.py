"""
Calculate the mass, volumen, temperature or presion of
ideal gases, from the equation:

    v = m/MRT/P;  n = m/M*N

v [L]             : volumen
m [g]             : mass
M [g/mol]         : molar mass
T [kelvin]        : temperature
P [atm]           : presion
R [L atm/(k mol)] : Molar gas constant
n                 : number of molecules
N [mol]           : Avogadro number
"""

import constants
from atomic_mass_percentage import split_symbols_amount, molecular_mass


# Constants
R: float = constants.constants["R"]
N: float = constants.constants["N"]


# Input by user
def read_temperature():
    "Read temperature from prompt"
    return float(input("temperature in kelvin of the ideal gas: "))


def read_mass():
    "Read mass from prompt"
    return float(input("massa in g of the ideal gas: "))


def read_presion():
    "Read presion from prompt"
    return float(input("presion in atm of the ideal gas: "))


def read_volumen():
    "Read volumen from prompt"
    return float(input("volumen in L of the ideal gas: "))


def calculate_amount(
    calculate: str, molar_mass: float
) -> tuple[str, float, str, float]:
    """
    Calculate the amount of unknown amount. Return its
    value with the respective units
    """

    if calculate.lower != "t":
        T: float = read_temperature()
    if calculate.lower() != "p":
        P: float = read_presion()
    if calculate.lower() != "m":
        m: float = read_mass()
    if calculate.lower() != "v":
        v: float = read_volumen()
    if calculate.lower() == "v":
        message: str = "volumen"
        amount: float = m / molar_mass * T * R / P
        unit: str = "L"
    elif calculate.lower() == "p":
        message = "presion"
        amount = m / molar_mass * T * R / v
        unit = "atm"
    elif calculate.lower() == "t":
        message = "temperature"
        amount = v * molar_mass / m * P / R
        unit = "k"
    else:
        message = "mass"
        amount = v * molar_mass * P / (T * R)
        unit = "g"

    # Massa
    if calculate.lower() == "m":
        m = amount

    # Number of molecules
    nmolecules: float = m / molar_mass * N

    return message, amount, unit, nmolecules


# Inputs
formule: str = input("what is the chemistry formule of the ideal gas?")
molar_mass: float = molecular_mass(split_symbols_amount(formule))

calculate: str = input("what amount does it calculate [v/m/T/P]?")

# Calculate
message, amount, unit, nmolecules = calculate_amount(calculate, molar_mass)

# Print results
print(f"\nThe {message} in the ideal gas is the {amount} {unit}")
print(f"Molecules amount {formule} is {nmolecules}")
