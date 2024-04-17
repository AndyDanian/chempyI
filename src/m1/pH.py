"""
Module 1 - Problem 4: acid-base titulation

Calculate for acid or base to reach the indicated pH:
    - volumen
    - normality

Moreover, it's possible calculated the pH.

Methodology:
    - Select the pH or what substance type to calculate
      its volumen or normality
    - Enter known quantities (normality, volumen, pH)
    - Calculate unknown volumen

NOTE:
    - When the substance under titulation is an acid with
      a base the pH increment
    - When the substance under titulation is a base with
      an acid the pH decrease
"""

from math import log10 as log


# Select calculate type
def calculation_type() -> int:
    """
    Drive the select incognit
    """
    incognit: int = int(
        input(
            """What do you want calculate [integer]?\n
                1 acid volumen\n
                2 base volumen\n
                3 acid normality\n
                4 base normality\n
                5 pH\n"""
        )
    )
    if incognit == 1:
        print("Calculation of acid volumen for base titualtion")
    if incognit == 2:
        print("Calculation of base volumen for acid titualtion")
    if incognit == 3:
        print(
            "Calculation acid normality in a acid-base solution at standard conditions"
        )
    if incognit == 4:
        print(
            "Calculation base normality in a acid-base solution at standard conditions"
        )
    if incognit == 5:
        print("Calculation of pH for a acid-base solution")
    return incognit


def verification(pH_titulation: float, pH: float, incognit: int) -> bool:
    """
    Verification of titulation process
    """

    if incognit == 1:
        # Acid titulation
        titulation: bool = pH_titulation > pH
    else:
        # Base titulation
        titulation = pH_titulation < pH

    return titulation


def input_parameters(
    incognit: int,
) -> tuple[float, float, float, float, float, float]:
    """
    Drive the input information
    """
    av: float = 0.0
    bv: float = 0.0
    an: float = 0.0
    bn: float = 0.0
    pH: float = 0.0
    size_volumen: float = 0.0

    if incognit != 1:
        av = float(input("what is the acid volumen?"))
        print(f"Acid Volumen: {av}")
    if incognit != 2:
        bv = float(input("what is the base volumen?"))
        print(f"Base Volumen: {bv}")
    if incognit != 3:
        an = float(input("what is the acid normality?"))
        print(f"Acid Normality: {an}")
    if incognit != 4:
        bn = float(input("what is the base normality?"))
        print(f"Base Normality: {bn}")
    if incognit != 5 and incognit in [1, 2]:
        pH = float(input("what is the desired pH?"))
        print(f"pH Desired: {pH}")
    if incognit in [1, 2]:
        size_volumen = float(
            input(
                "what is the volumen size in each \
                                   titulation step?"
            )
        )
        print(f"Titulation Step: {size_volumen}")

    return av, bv, an, bn, pH, size_volumen


def calculation(incognit: int) -> None:
    """
    Drive the titulation calculation
    """

    av, bv, an, bn, pH, size_volumen = input_parameters(incognit)
    v_titulation: float = 0.0

    if incognit in [1, 2]:
        # * Titulation process selected
        substance_a: str = "acid"
        substance_b: str = "base"
        norm_sub_a: float = an
        norm_sub_b: float = bn
        vol_sub_a: float = av
        if incognit == 1:
            substance_a = "base"
            substance_b = "acid"
            norm_sub_a = bn
            norm_sub_b = an
            vol_sub_a = bv

        pH_titulation: float = 0.0
        while verification(pH_titulation, pH, incognit):
            n_temp: float = norm_sub_a - norm_sub_b * v_titulation / vol_sub_a
            if n_temp > 0.0:
                # * acid normality in excess
                pH_titulation = -log(n_temp)
            elif round(n_temp, 2) == 0.0:
                # * neutralization of pH: [H+] = [OH-]
                pH_titulation = 7.0
            else:
                # * base normality excess
                n_temp = norm_sub_b * v_titulation / (vol_sub_a + v_titulation)
                pH_titulation = 14 + log(n_temp)
            print(
                f"{substance_a} normality: {round(n_temp,2)},\
                    {substance_b} volumen: {round(v_titulation,2)},\
                    pH titulation: {round(pH_titulation,2)}"
            )
            v_titulation += size_volumen

    elif incognit == 3:
        # * Acid normality calcuation selected
        acid_normality: float = bn * bv / av
        print(f"Acid Normality: {acid_normality}")
    elif incognit == 4:
        # * Base normality calcuation selected
        base_normality: float = bn * bv / av
        print(f"Base Normality: {base_normality}")
    else:
        # * pH calcuation selected
        solution_normality: float = (an * av) - (bn * bv)
        if solution_normality < 0.0:
            print(
                f"Solution has excess of [OH-] and its pH: \
                {14 + log(bn * bv/(av + bv))}"
            )
        else:
            print(f"Solution has excess of [H+] and its pH: \
                {-log(an * av/(av + bv))}")


if __name__ == "__main__":
    # Select Calculation Type
    incognit = calculation_type()
    # Run Calculation
    calculation(incognit)
