"""
This program ask user a chemistry formule. After that to
split the atomic symbol and number in next step. Then,
it joins the atomic symbols that is repated and finally,
sums the mass and shows the porcentages.
"""

from atomic_number_mass import atomic_number_mass as Zm


def split_symbols_amount(mol_formule: str = "") -> dict[str, int]:
    """
    build a dictionary with the atomic symbols and amount
    for each atom
                {atomic_symbol: amount, ...}

    >>> 'C2CH6H2' -->  {'C': 3, 'H': 6}
    """
    # split molecular formule
    atomic_symbols: list[str] = []
    atoms_amount_tmp: list[str] = []
    for abc in mol_formule:
        if abc.isupper():  # it is the capitalize string
            atoms_amount_tmp.append("")
            atomic_symbols.append(abc)
        if abc.islower():  # it is not the capitalize string
            atomic_symbols[-1] += abc
        if abc.isnumeric():  # it is the string a number
            atoms_amount_tmp[-1] += abc

    # convert string to int and transform '' to 1
    atoms_amount: list[int] = [int(i) if i != "" else 1 for i in atoms_amount_tmp]
    # build a dictionary where the keys is the atomic symbols while the
    # value is equal 0
    composition: dict[str, int] = {symbol: 0 for symbol in atomic_symbols}

    # remplace 0 by the amount of atoms in the molecular formule
    for s, a in zip(atomic_symbols, atoms_amount):
        composition[s] += a

    return composition


def molecular_mass(composition: dict[str, int]) -> float:
    """
    Calculate the Molecular Mass
    """

    molecular_mass: float = 0.0
    for symbol, amount in composition.items():
        molecular_mass += amount * Zm[symbol][1]

    return molecular_mass


def porcentage_mass(
    mol_formule: str, composition: dict[str, int], molar_mass: float
) -> None:
    """
    Calculate the porcentage of mass by each atom in
    the molecular formule
    """
    print(f"Molecular mass of {mol_formule} is {molar_mass}")
    for symbol, amount in composition.items():
        print(f"Atomic mass % of {symbol} is\
                        {round(amount * Zm[symbol][1]*100/molar_mass,3)}")


if __name__ == "__main__":
    # input the molecular formule by user
    mol_formule = input("Write the Molecular Formule of Whatever Substance: ")

    # split information in the molecular formule
    composition = split_symbols_amount(mol_formule)

    # print molecular mass
    molar_mass = molecular_mass(composition)

    # porcentages
    porcentage_mass(mol_formule, composition, molar_mass)
