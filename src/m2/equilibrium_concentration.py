"""
Module 2 - Problem 3: Concentration in Equilibrium Reaction

This program calculate the concentration of the substance in an equilibrium
reaction from the reactives concentration before the reaction start.

NOTE:
This program only work with reactions which have two reactives and two products
"""

import numpy as np


def input_mol_concent() -> tuple[list[str], list[float], float]:
    """
    Input the molecular information and equilibrium constant, K.
    """
    molecules: list[str] = []
    concent_react: list[float] = []

    print("Input the molecular information\n")
    print("Reactives: ")
    for r in range(2):
        molecules.append(input(f"{r+1}: "))
        concent_react.append(float(input(f"Concentration of {molecules[r]}: ")))

    print("\nProducts: ")
    for p in range(2):
        molecules.append(input(f"{p+1}: "))

    K: float = float(input("what is the equilibrium constant?\n"))

    return molecules, concent_react, K


def cofficients(concent_react: list[float], K: float) -> list[float]:
    """
    Calculate the coefficient
    """

    a: float = K - 1.0
    b: float = K * (concent_react[0] + concent_react[1])
    c: float = K * (concent_react[0] * concent_react[1])

    return [a, -b, c]


def getroots(coefficients: list[float], concent_react: list[float]) -> list[float]:
    """ """

    roots: list[float] = []
    for r in np.roots(coefficients):
        if r < concent_react[0] and r < concent_react[1]:
            roots.append(r)

    return roots


def concentrations(concent_react: list[float], roots: list[float]):
    """
    Get the equlibrium concentraions for reactives and products
    """

    equi_concent: list[list[float]] = []
    for r in roots:
        equi_concent.append([concent_react[0] - r, concent_react[1] - r, r, r])

    return equi_concent


if __name__ == "__main__":
    # * Input
    molecules, concent_react, K = input_mol_concent()

    # * Calculation of coefficient
    coefficients = cofficients(concent_react, K)

    # * Get roots
    roots = getroots(coefficients, concent_react)

    # * Get equilibrum concentrations
    equ_conc = concentrations(concent_react, roots)

    # * Output
    print()
    print("=" * 25, "Result", "=" * 25)

    print(f"{molecules[0]}  +  {molecules[0]}  =  {molecules[2]}  +  {molecules[3]}")
    print("Equilibrium Concentrations: ")
    for conc in equ_conc:
        for m, c in zip(molecules, conc):
            print(f"{m}: {np.round(c,3)}")

    print("="*58)

# """
# try:
# Input the molecular information
# Reactives:
# 1: CH3COOH
# Concentration of CH3COOH: 1
# 2: C2H5OH
# Concentration of CH3COOH: 8
# Products:
# 1: CH3COOC2H5
# 2: H2O
# what is the equilibrium constant?4
# """