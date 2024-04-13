import constants
from atomic_mass_percentage import split_symbols_amount, molecular_mass

"""
Calculate the mass, volumen, temperature or presion of
an ideal gas, from the equation:

    v = m/MRT/P;  n = m/M*N

v [L]      : volumen
m [g]      : mass
M [g/mol]  : molar mass
T [kelvin] : temperature
P [atm]    : presion
R [L atm/(k mol)] : Molar gas constant
n []       : number of molecules
N [mol]    : Avogadro number
"""

# Constants
R = constants.constants["R"]
N = constants.constants["N"]

# Input by user
def read_temperature():
    return float(input("temperature in kelvin of the ideal gas: "))
def read_mass():
    return float(input("massa in g of the ideal gas: "))
def read_presion():
    return float(input("presion in atm of the ideal gas: "))
def read_volumen():
    return float(input("volumen in L of the ideal gas: "))

# Calculate
def calculate_amount(calculate: str, molar_mass: float):
    """
    Calculate the amount ask and also, return its units
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
        message = "the volumen"
        amount = m/molar_mass*T*R/P
        unit = "L"
    elif calculate.lower() == "p":
        message = "the presion"
        amount = m/molar_mass*T*R/v
        unit = "atm"
    elif calculate.lower() == "t":
        message = "the temperature"
        amount = v*molar_mass/m*P/R
        unit = "k"
    else:
        message = "the mass"
        amount = v*molar_mass*P/(T*R)
        unit = "g"    
    if calculate.lower() == "m":
        m = amount
    nmolecules: float = m/molar_mass*N
    return message, amount, unit, nmolecules

# 
formule = input("what is the chemistry formule of the ideal gas?")
molar_mass = molecular_mass(split_symbols_amount(formule))

calculate = input("what amount does it calculate [v/m/T/P]?")

# Calculate
message, amount, unit, nmolecules = calculate_amount(calculate,molar_mass)

# Print results
print(f"{message} in the ideal gas is the {amount} {unit}")
print(f"amount the molecules: {nmolecules} of {formule}")
