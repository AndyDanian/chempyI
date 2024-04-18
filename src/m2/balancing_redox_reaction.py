"""
# Module 2 - Problem 7: Balancing an redox reaction

Indetify the substances that is oxidized from the reduced of a reaction
with two reactives and two products. Moreover, the oxidation number of
the same atom in the both reactives or products should be equal. This
program can also calculate the oxidation number of one atom in a molecule

Methodology:
    - Input reactants and products with their charges
    - Input oxidation numbers
    - Calculate of oxidation number
    - Electronic movement
    - Classify the substance in reducing and oxidizing agents

NOTE (future editions):
    - Oxidation number: is a virtual charge belong to an atom whether every
      bonds are ionic
    - An atom of free element has an oxidation number equal to 0, example,
      each atom in Cl2
    - An monoatomic ion has an oxidation number equal to the charge
    - Alkali metals in a molecule always have an oxidation number equal to 1
    - Alkali earth metals in a molecule always have an oxidation number equal
      to 2
    - Fluorine in compounds has an oxidation number equal to -1
    - Hydrogen in compoinds has an oxidation number equal to 1 except in
      molecules with metals because in these substances its oxidation number
      equal to -1, example, NaH
    - Oxygen atom has an oxidation number equal to -2 except in the peroxide
      because in this substance its oxidation number is equal to -1
    - Other halogens have an oxidation number equal to -1 but in molecules
      with oxygen or fluorine its oxidation number change, example, ClO4- the
      Cl is 7
"""

from sys import path
import numpy as np

path.append("../m1")
from atomic_mass_percentage import split_symbols_amount, molecular_mass


def molecule_composition(molecule: list) -> [str, int]:
    """
    Yet one generator (iterator) with the molecular labels
    """
    for m in molecule:
        yield split_symbols_amount(m)


def input_molecules() -> tuple[list[str], list[int], list[dict[str, int]], int, int]:
    """
    Drive the input information and molecular labels
    >>> CH4
    Moreover, count the number of atoms type in each molecule
    to return: dictionary{atom: amount}
    """

    # input information
    num_react: int = int(input("how many reactives are there? "))
    num_prod: int = int(input("how many products are there? "))

    molecules: list[str] = []
    charges: list[int] = []
    print("\nReactive:")
    for r in range(num_react):
        molecules.append(input(f"{r+1}: "))
        charges.append(int(input(f"charge ({molecules[r]}): ")))

    print("\nProduct:")
    for p in range(num_prod):
        molecules.append(input(f"{p+1}: "))
        charges.append(int(input(f"charge ({molecules[num_react+p]}): ")))
    print()

    # split atomic information
    comp_react_prod: list[dict[str, int]] = [
        comp for comp in molecule_composition(molecules)
    ]

    return molecules, charges, comp_react_prod, num_react, num_prod


def calculate_oxidation_number(
    molecule_composition: dict[str, int], oxidation_number: dict[str, int], charge: int
) -> dict[str, int]:
    """
    Calculate of oxidation number for atoms with 999 like
    oxidation number
    """
    for atom, no in oxidation_number.items():
        if no == 999:
            num_at: int = molecule_composition[atom]
            temp: int = charge - sum(
                [
                    on * na
                    for na, on in zip(
                        molecule_composition.values(), oxidation_number.values()
                    )
                    if on != 999
                ]
            )
            temp = temp // num_at
            oxidation_number[atom] = temp

    return oxidation_number


def input_oxidation_number(
    molecules_composition: list[dict[str, int]],
    molecules: list[str],
    charges: list[int],
) -> dict[str, int]:
    """
    Input oxidation number and calculate the unkown oxidation numbers
    """
    for count, mol in enumerate(molecules_composition):
        oxidation_number: dict[str, int] = {}
        for atom in mol.keys():
            oxidation_number[atom] = int(
                input(
                    f"what is the oxidation number of atom {atom} in {molecules[count]}? "
                )
            )

        if 999 in oxidation_number.values():
            oxidation_number = calculate_oxidation_number(
                mol, oxidation_number, charges[count]
            )

        yield oxidation_number


def oxidation_number(
    molecules_composition: list[dict[str, int]],
    molecules: list[str],
    charges: list[int],
) -> list[dict[str, int]]:
    """
    Drive the input or calculation of oxidation number
    """
    print("if you unknown the oxidation number, please input 999 and the")
    print("program try calculate it (maximum one atom by molecule)\n")
    return [
        no for no in input_oxidation_number(molecules_composition, molecules, charges)
    ]


def redox(
    react: dict[str, int], prod: dict[str, int], r: str, p: str, cr: int, cp: int
) -> dict[str, int]:
    """
    Calculate the change in the amount of electrons and classify
    of molecule in oxidizing or reducing agent
    """

    oxidation_numbers: dict[str, int] = {}
    for atr, onr in react.items():
        if atr in prod.keys():
            if prod[atr] > onr:
                print(f"The atom {atr} oxidizes when pass")
                print(f"from {r}^({cr}) to {p}^({cp}) ({onr}-->{prod[atr]})")
                oxidation_numbers[atr] = prod[atr] - onr
                oxidation_numbers["Oxidize"] = True
            elif prod[atr] == onr:
                print(f"The atom {atr} doesn't suffer redox reaction")
                print(f" when pass from {r}^({cr}) to {p}^({cp})")
            else:
                print(f"The atom {atr} reduces when pass")
                print(f" from {r}^({cr}) to {p}^({cp}) ({onr}-->{prod[atr]})")
                oxidation_numbers[atr] = onr - prod[atr]
                oxidation_numbers["Oxidize"] = False
            print()

    return oxidation_numbers


def oxide_reduction_description(
    no_react_prod: list[dict[str, int]],
    charges: list[int],
    molecules: list[str],
    num_react: int,
    num_prod: int,
) -> dict[str, int]:
    """
    Yet the description of each one molecule like oxidizing or
    reducing agent
    """
    for r in range(num_react):
        react: dict[str, int] = no_react_prod[r]
        for p in range(num_prod):
            prod: dict[str, int] = no_react_prod[p + num_react]

            redox_numbers = redox(
                react,
                prod,
                molecules[r],
                molecules[p + num_react],
                charges[r],
                charges[p + num_react],
            )

            if len(redox_numbers) > 0:
                yield redox_numbers


def oxide_reduction(
    no_react_prod: list[dict[str, int]],
    charges: list[int],
    molecules: list[str],
    num_react: int,
    num_prod: int,
) -> list[dict[str, int]]:
    """
    Drive the classification of molecules in oxidizing and
    reducing agent. Moreover, the difference the electrons
    between reactives and products
    """
    print("*"*56)
    list_oxidation_numbers: list[dict[str, int]] = [
        diff_no
        for diff_no in oxide_reduction_description(
            no_react_prod, charges, molecules, num_react, num_prod
        )
    ]
    print("*"*56)
    return list_oxidation_numbers


def heaviest(molecules: list[dict[str, int]]) -> int:
    """
    Find the heaviest molecule, because it's neccesary
    when the matrix is not square, then is add the row
    or column of the heaviest molecule to transform the
    matrix in square and balance the chemical reactiong
    """

    heaviest_index: int = 0
    heaviest: float = 0.0
    for count, mol in enumerate(molecules):
        mass_mol: float = molecular_mass(mol)
        if mass_mol > heaviest:
            heaviest = mass_mol
            heaviest_index = count

    return heaviest_index


def add_row_col(matrix: np.array, heaviest: int, nrow: int, ncol: int) -> np.array:
    """
    Add the information of the heaviest molecule another
    time like row or column to build a square matrix
    """

    if nrow > ncol:
        column_add = np.array(
            [0 if i < (nrow - 1) else 1 for i in range(nrow)], dtype=np.float_
        )
        return np.column_stack((matrix, column_add))
    else:
        row_add = np.array(
            [1 if i == heaviest else 0 for i in range(ncol)], dtype=np.float_
        )
        return np.r_[matrix, [row_add]]


def matrix_amount_charge(
    comp_react_prod: list[dict[str, int]],
    charges: list[int],
    num_r: int,
) -> tuple[np.array, np.array]:
    """
    Build a matrix (type np.array) square

    - Each column is associated with the amount of a atom type
    - Each row is associated to a molecule

    molecule1 -> | atom1 atom2 ... atomN  |
                 |   .     .   ...   .    |
                 |   .     .   ...   .    |
                 |   .     .   ...   .    |
    moleculeN -> | atom1 atom2 ... atomN  |

    Moreover, this function builds the matrix b necessay to balance
    process

    NOTE:
    The reactive coefficient are also positive because negative values
    make mistake in some reaction, for example
    # Fe⁺² + Cr2O7⁺² + H⁺¹ --> Cr⁺³ + H2O + Fe⁺³
    """

    # Atoms array
    atoms: set[str] = {
        atom for molecule in comp_react_prod[:num_r] for atom in molecule.keys()
    }

    # Build matrix
    matrix_list: list[list[int]] = []
    for a in atoms:
        temp: list[int] = []
        for molecule in comp_react_prod:
            if a in molecule.keys():
                temp.append(molecule[a])
            else:
                temp.append(0)
        matrix_list.append(temp)
    matrix_list.append(charges)

    matrix = np.array(matrix_list, dtype=np.float_)

    # * Verification what matrix is square
    row, col = matrix.shape
    if row == col:
        print(f"The matrix with amount of the atoms is square: {row} x {col}")
        matrix_square = matrix
        coef_result = np.array([0 for i in range(row)], dtype=np.float_)
    else:
        print(f"The matrix with amount of the atoms is not square: {row} x {col}")
        message: str = "col"
        n: int = row
        if col > row:
            message = "row"
            n = col

        print(f"Then, is add one {message} in the last")
        heaviest_molecule = heaviest(comp_react_prod)

        matrix_square = add_row_col(matrix, heaviest_molecule, row, col)

    coef_result = np.array([0 if i < (n - 1) else 1 for i in range(n)], dtype=np.float_)

    return matrix_square, coef_result


def redox_balance(mat_comp_mol: np.array, coef_result: np.array) -> np.array:
    """
    Return the coefficient to balance the chemical reaction
    """
    return np.linalg.solve(mat_comp_mol, coef_result)


if __name__ == "__main__":
    # aFe⁺² + bCr2O7⁺² + cH⁺¹ --> dCr⁺³ + eH2O + fFe⁺³
    # * Input molecules
    molecules, charges, comp_react_prod, num_react, num_prod = input_molecules()

    # * Input oxidation number
    num_oxid_atoms_react_prod = oxidation_number(comp_react_prod, molecules, charges)

    # * Oxidize and reduction classifycation
    oxidation_type = oxide_reduction(
        num_oxid_atoms_react_prod, charges, molecules, num_react, num_prod
    )

    # * Build: matrix
    matrix_square_atoms, coef_result = matrix_amount_charge(
        comp_react_prod, charges, num_react
    )

    # * Balance
    balance_coeff = redox_balance(matrix_square_atoms, coef_result)

    # * Output
    print()
    print("=" * 25, "Result", "=" * 25)
    print(f"Balance coeffecients from reactives and products:\n {balance_coeff}")
    print("\nChemical formule:")
    chem_formule: str = ""
    for count, molecule in enumerate(molecules):
        bc: str = ""
        if abs(balance_coeff[count]) > 1:
            bc = str(abs(round(balance_coeff[count], 1)))
            chem_formule += bc + " " + molecule + "^" + str(charges[count])

        if (
            count < num_react - 1
            or count >= num_react
            and count < num_react + num_prod - 1
        ):
            chem_formule += " + "

        if count == num_react - 1:
            chem_formule += " --> "
    print(chem_formule.center(58))

    print()

    for ox_red in oxidation_type:
        oxid_red: str = "oxidize"
        lost_gain: str = "lost"
        if not ox_red["Oxidize"]:
            oxid_red = "reduce"
            lost_gain = "gain"
        print(
            f"The atom {list(ox_red.keys())[0]} is {oxid_red}, {lost_gain} {list(ox_red.values())[0]} electrons"
        )
    print("=" * 58)
