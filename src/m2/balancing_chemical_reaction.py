"""
# Module 2 - Problem 1: Balancing a Chemical Reaction

This problem consists in look for the coefficients to balance the
chemical reaction with the solution a set of lineal equation

                        X = A⁻¹b
Where:
    - A is a square matrix with the amount of the atoms in each molecule
    - b is a vector
    - X is a vector with the coefficients to balance the chemical reaction
"""

from sys import path
import numpy as np

path.append("../m1")
from atomic_mass_percentage import split_symbols_amount, molecular_mass


def input_molecules() -> tuple[list[str], list[dict[str, int]], int, int]:
    """
    Drive the input information and molecular labels
    >>> CH4
    Moreover, count the number of atoms type in each molecule
    to return: dictionary{atom: amount}
    """

    # input information
    num_react: int = int(input("how many reactives are there? "))
    num_prod: int = int(input("how many products are there? "))

    print("\nReactive:")
    list_react_prod: list[str] = []
    for r in range(num_react):
        list_react_prod.append(input(f"{r+1}: "))

    print("\nProduct:")
    for p in range(num_prod):
        list_react_prod.append(input(f"{p+1}: "))
    print()

    # split atomic information
    comp_react_prod: list[dict[str, int]] = [
        comp for comp in molecule_composition(list_react_prod)
    ]

    return list_react_prod, comp_react_prod, num_react, num_prod


def molecule_composition(molecule: list) -> [str, int]:
    """
    Yet one generator (iterator) with the molecular labels
    """
    for m in molecule:
        yield split_symbols_amount(m)


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
        column_add: np.array = np.array(
            [0 if i < (nrow - 1) else 1 for i in range(nrow)], dtype=np.float_
        )
        return np.column_stack((matrix, column_add))
    else:
        row_add: np.array = np.array(
            [1 if i == heaviest else 0 for i in range(ncol)], dtype=np.float_
        )
        return np.r_[matrix, [row_add]]


def matrix_amount_atom(
    comp_react_prod: list[dict[str, int]], num_r: int
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
    """

    # Atoms array
    atoms: set[str] = {
        atom for molecule in comp_react_prod[:num_r] for atom in molecule.keys()
    }

    # Build matrix
    matrix_amount_atoms: list[list[int]] = []
    for a in atoms:
        temp: list[int] = []
        for count, molecule in enumerate(comp_react_prod):
            if a in molecule.keys() and count < num_r:
                temp.append(molecule[a])
            elif a in molecule.keys() and count >= num_r:
                temp.append(-molecule[a])
            else:
                temp.append(0)
        matrix_amount_atoms.append(temp)

    matrix = np.array(matrix_amount_atoms, dtype=np.float_)

    # * Verification what matrix is square
    row, col = matrix.shape
    if row == col:
        print(f"The matrix with the atoms amount is square: {row} x {col}")
        matrix_square = matrix
        coef_result = np.array([0 for i in range(row)], dtype=np.float_)
    else:
        print(f"The matrix with the atoms amount is not square: {row} x {col}")
        message: str = "col"
        n: int = row
        if col > row:
            message = "row"
            n = col

        print(f"Then, is add one {message} in the last")
        heaviest_molecule = heaviest(comp_react_prod)

        matrix_square = add_row_col(matrix_amount_atoms, heaviest_molecule, row, col)

        coef_result = np.array(
            [0 if i < (n - 1) else 1 for i in range(n)], dtype=np.float_
        )

    return matrix_square, coef_result


def balance(mat_comp_mol: np.array, coef_result: np.array) -> np.array:
    """
    Return the coefficient to balance the chemical reaction
    """
    return np.linalg.solve(mat_comp_mol, coef_result)


if __name__ == "__main__":
    # * Input
    list_react_prod, comp_react_prod, num_react, num_prod = input_molecules()

    # * Build: matrix
    matrix_square_atoms, coef_result = matrix_amount_atom(comp_react_prod, num_react)

    # * Balance
    balance_coeff = balance(matrix_square_atoms, coef_result)

    # * Output
    print()
    print("=" * 25, "Result", "=" * 25)
    print(f"Balance coeffecients from reactives and products:\n {balance_coeff}")
    print("\nChemical formule:")
    chem_formule: str = ""
    for count, molecule in enumerate(list_react_prod):
        bc: str = ""
        if balance_coeff[count] > 1:
            bc = str(balance_coeff[count])
        chem_formule += bc + " " + molecule

        if (
            count < num_react - 1
            or count >= num_react
            and count < num_react + num_prod - 1
        ):
            chem_formule += " + "

        if count == num_react - 1:
            chem_formule += " --> "
    print(chem_formule.center(58))
    print("=" * 58)

    # Try:
    # aCO2 + bH2O -->  cC6H12O6 + dO2
    # aH2 + bO2 --> cH2O
