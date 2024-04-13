"""
This program ask user a chemistry formule, to split the 
atomic symbol and number in next step. Then, it joins 
the atomic symbols that is repated and finally, sums the 
mass and shows the porcentages.
"""
from atomic_number_mass import atomic_number_mass as Zm


def split_symbols_amount(mol_formule: str):
    """
    build a dictionary with the atomic symbols and amount
    for each atom
                {atomic_symbol: amount, ...}
    """
    atomic_symbols: list[str] = []
    atoms_amount_tmp: list[str] = []
    for abc in mol_formule:
        if abc.isupper():  # is the string capitalize
            atoms_amount_tmp.append('')
            atomic_symbols.append(abc)
        if abc.islower():  # is not the string capitalize
            atomic_symbols[-1] += abc
        if abc.isnumeric():  # is the string a number
            atoms_amount_tmp[-1] += abc
    # convert string to int and transform '' to 1
    atoms_amount: list[int] = [int(i) if i != '' else 1 for i in atoms_amount_tmp]
    # build a dictionary where the keys is the atomic symbols while the value is equal 0  
    composition: dict[str: int] = {symbol: 0 for symbol in atomic_symbols}
    # remplace 0 by the amount of atoms in the molecular formule 
    for symbol, amount in zip(atomic_symbols, atoms_amount):
        composition[symbol] += amount
    return composition

def molecular_mass(composition: dict[str: int]):
    # molecular mass
    molecular_mass: float = 0.
    for symbol, amount in composition.items():
        molecular_mass += amount*Zm[symbol][1]
    return molecular_mass


if __name__ == "__main__":
    # input the molecular formule by user
    mol_formule: str = input("Write the Molecular Formule of Whatever Substance: ")
    # split information in the molecular formule
    composition = split_symbols_amount(mol_formule)
    # print molecular mass
    molar_mass = molecular_mass(composition)
    print(f"Molecular mass of {mol_formule} is {molar_mass}")
    # porcentages
    for symbol, amount in composition.items():
        print(f"Atomic mass % of {symbol} is {round(amount*Zm[symbol][1]*100/molar_mass,3)}")


