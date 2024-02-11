"""
Module 1 - Problem 8: Signs number and intesities relations

This program determine the number of signs and their relations in a spin-spin coupling spectrum with the Pascal's triangle.

    * Input number of nucleus equivalents
    * Use the factorial function which is a recurrence to calculation 
"""

def factorial(number: int) -> int:

    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

def spin_spin_sign(atoms_number: int) -> list:

    if atoms_number == 1:
        return [1]
    else:
        list_sign: list[int] = [1]
        for n in range(atoms_number - 2):
            list_sign.append(factorial(atoms_number-1)/(factorial(atoms_number-(n+2))*factorial(n+1)))
        list_sign.append(1)
    return list_sign

if __name__ == "__main__":
    atoms_number: int = int(input("what is the atoms number? "))
    sign_number = spin_spin_sign(atoms_number)
    print(f"The number of signes produce by {atoms_number} equivalent atoms is: {len(sign_number)}")
    print(f"The relation of intesities among signed is: {sign_number}")