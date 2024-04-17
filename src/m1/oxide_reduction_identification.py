"""
Module 1 - Problem 5: Oxide-Reduction Identification

Indetify the substances that is oxidized from the reduced of a reaction
with two reactives and two products.

Moreover, the oxidation number of the same atom in the both reactives or
products should be equal. This program can also calculate the oxidation
number of one atom in a molecule

Process:
    - Input reactants and products with their charges
    - Input oxidation numbers
    - Calculate of oxidation number
    - Electronic movement
    - Classify the substance in reducing and oxidizing agents

NOTE (future editions or tasks):

    - Oxidation number: is a virtual charge belong to an atom whether every
      bonds are ionic
    - An atom of free element has an oxidation number equal to 0, example,
      each atom in Cl2
    - A monoatomic ion has an oxidation number equal to the charge
    - Alkali metals in a molecule always have an oxidation number equal to 1
    - Alkali earth metals in a molecule always have an oxidation number equal
      to 2
    - Fluorine in compounds has an oxidation number equal to -1
    - Hydrogen in compoinds has an oxidation number equal to 1 except in
      molecules with metals because in these substances its oxidation number
      equal to -1, example, NaH
    - Oxygen atom has an oxidation number equal to -2 except in the peroxide
      because in this substance its oxidation number is equal to -1
    - Other halogens have an oxidation number equal to -1 but in molecules with
      oxygen or fluorine its oxidation number change, example, ClO4- the Cl is
      7
"""

from atomic_mass_percentage import split_symbols_amount


def input_substance() -> tuple[str, int, str, int, str, int, str, int]:
    """
    Input information from the prompt:
        - Reactives and charges
        - Products and charges
    """
    reactive_a: str = input("what is the first reactive and its charge?")
    r_charge_a: int = int(input(f"what is the charge of the {reactive_a}?"))

    reactive_b: str = input("what is the second reactive and its charge?")
    r_charge_b: int = int(input(f"what is the charge of the {reactive_b}?"))

    product_a: str = input("what is the first product and its charge?")
    p_charge_a: int = int(input(f"what is the charge of the {product_a}?"))

    product_b: str = input("what is the second product and its charge?")
    p_charge_b: int = int(input(f"what is the charge of the {product_b}?"))

    return (
        reactive_a,
        r_charge_a,
        reactive_b,
        r_charge_b,
        product_a,
        p_charge_a,
        product_b,
        p_charge_b,
    )


def input_oxidation_number(
    molecule_composition: dict[str, int], molecule: str, charge: int
) -> dict[str, int]:
    """
    Input oxidation number
    """
    oxidation_number: dict[str, int] = {}
    for atom in molecule_composition.keys():
        oxidation_number[atom] = int(
            input(f"what is the oxidation number of atom {atom} in {molecule}?\n")
        )

    if 999 in oxidation_number.values():
        oxidation_number = calculate_oxidation_number(
            molecule_composition, oxidation_number, charge
        )

    return oxidation_number


def calculate_oxidation_number(
    molecule_composition: dict[str, int], oxidation_number: dict[str, int], charge: int
) -> dict[str, int]:
    """
    Oxidation number by each atom is calcularet if the atom don't have
    """

    for atom, no in oxidation_number.items():
        if no == 999:
            oxidation_number[atom] = charge - sum(
                [
                    on * na
                    for na, on in zip(
                        molecule_composition.values(), oxidation_number.values()
                    )
                    if on != 999
                ]
            )

    return oxidation_number


def oxide_reduction(
    react: dict[str, int], prod: dict[str, int], mol_a: str, mol_b: str
) -> dict[str, int]:
    """
    Classify the substances according like the electrons moving in the
    reaction
    """

    oxidation_numbers: dict[str, int] = {}
    for atr, onr in react.items():
        if atr in prod.keys():
            if prod[atr] > onr:
                print(
                    f"The atom {atr} oxidizes when pass from {mol_a} to {mol_b} ({onr}-->{prod[atr]})"
                )
                oxidation_numbers[atr] = [prod[atr] - onr]
                oxidation_numbers["Oxidize"] = True
            elif prod[atr] == onr:
                print(
                    f"The atom {atr} doesn't suffer oxide-reduction reaction  when pass from {mol_a} to {mol_b}"
                )
            else:
                print(
                    f"The atom {atr} reduces when pass from {mol_a} to {mol_b} ({onr}-->{prod[atr]})"
                )
                oxidation_numbers[atr] = [onr - prod[atr]]
                oxidation_numbers["Oxidize"] = False

    return oxidation_numbers


if __name__ == "__main__":
    # Example of inputs
    reactive_a = "HNO3"
    reactive_b = "Sn"
    product_a = "H2SnO3"
    product_b = "NO"
    r_charge_a = r_charge_b = p_charge_a = p_charge_b = 0

    # Amount: each one the atoms
    comp_react_a = split_symbols_amount(reactive_a)
    comp_react_b = split_symbols_amount(reactive_b)
    comp_prod_a = split_symbols_amount(product_a)
    comp_prod_b = split_symbols_amount(product_b)

    # Oxidation number (input/calculations)
    print("if you unknown the oxidation number, please input 999 and", end="")
    print(" the program calculate it (only maximum one atom by molecule)")

    print("\n", "*" * 60, "\n")
    num_oxid_atoms_react_a = input_oxidation_number(
        comp_react_a, reactive_a, r_charge_a
    )
    num_oxid_atoms_react_b = input_oxidation_number(
        comp_react_b, reactive_b, r_charge_b
    )
    num_oxid_atoms_prod_a = input_oxidation_number(comp_prod_a, product_a, p_charge_a)
    num_oxid_atoms_prod_b = input_oxidation_number(comp_prod_b, product_b, p_charge_b)

    # Output oxidation number
    print("\n", "*" * 60, "\n")
    print(f"Number of oxidation of atoms in the {reactive_a}: {num_oxid_atoms_react_a}")
    print(f"Number of oxidation of atoms in the {reactive_b}: {num_oxid_atoms_react_b}")
    print(f"Number of oxidation of atoms in the {product_a}: {num_oxid_atoms_prod_a}")
    print(f"Number of oxidation of atoms in the {product_b}: {num_oxid_atoms_prod_b}")

    # Output classification of substances
    print("\n", "*" * 60, "\n")
    nums_oxid_a_a = oxide_reduction(
        num_oxid_atoms_react_a, num_oxid_atoms_prod_a, reactive_a, product_a
    )
    nums_oxid_a_b = oxide_reduction(
        num_oxid_atoms_react_a, num_oxid_atoms_prod_b, reactive_a, product_b
    )
    nums_oxid_b_a = oxide_reduction(
        num_oxid_atoms_react_b, num_oxid_atoms_prod_a, reactive_b, product_a
    )
    nums_oxid_b_b = oxide_reduction(
        num_oxid_atoms_react_b, num_oxid_atoms_prod_b, reactive_b, product_b
    )
