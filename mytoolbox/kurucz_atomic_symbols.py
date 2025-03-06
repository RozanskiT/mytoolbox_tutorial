from typing import Union, Tuple

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
ATOMIC_NUMBERS = {
    1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
    11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca',
    21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
    31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr',
    41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn',
    51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd',
    61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb',
    71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg',
    81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th',
    91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm',
    101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt',
    110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'
}
"""
Mapping of atomic numbers (integers) to their corresponding chemical symbols (strings).
"""

SYMBOLS = {symbol: num for num, symbol in ATOMIC_NUMBERS.items()}
"""
Reverse mapping of chemical symbols (strings) to their atomic numbers (integers).
"""

ION_STAGES = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"
]
"""
List of possible ionization stages represented as Roman numerals (I, II, III, etc.).
"""

def kurucz_code_to_symbol(code: Union[float, str]) -> str:
    """
    Convert a Kurucz code to a human-readable format of "Symbol IonStage".

    A Kurucz code generally has the form 'ZZ.ZZ', where:
    - ZZ (integer part) = atomic number.
    - ZZ (decimal part times 100) = ionization stage index (0-based).

    For example, a code of 26.00 would translate to "Fe I", and 26.01 to "Fe II".

    Args:
        code (Union[float, str]): The Kurucz code, either as a float or a string.

    Returns:
        str: A string in the format "<ElementSymbol> <IonStage>", for example "Fe II".
             If the atomic number or ion stage is not found in the predefined lists,
             they are replaced with placeholders such as "Z=<atomic_number>" or
             "IonStage=<ion_stage>".
    """
    code_float = float(code)
    atomic_num = int(code_float)
    ion_stage = int(round((code_float - atomic_num) * 100))

    symbol = ATOMIC_NUMBERS.get(atomic_num, f"Z={atomic_num}")
    ion_str = ION_STAGES[ion_stage] if ion_stage < len(ION_STAGES) else f"IonStage={ion_stage}"
    return f"{symbol} {ion_str}"

def symbol_to_kurucz_code(symbol_str: str) -> str:
    """
    Convert a string of the form "<ElementSymbol> <IonStage>" to a Kurucz code.

    The function first parses the symbol and the ion stage from the given string
    using `parse_symbol_and_ion()`. It then constructs a code by combining
    the atomic number and the ion stage index in the form ZZ.xx, where:
    - ZZ = atomic number
    - xx = zero-padded ion stage index

    For example, "Fe II" would become "26.01", and "Fe I" would become "26.00".

    Args:
        symbol_str (str): The element symbol and ion stage, e.g., "Fe II".

    Returns:
        str: The Kurucz code, for example "26.01".

    Raises:
        ValueError: If the element symbol is not recognized.
    """
    symbol, ion_stage = parse_symbol_and_ion(symbol_str)

    if symbol not in SYMBOLS:
        raise ValueError(f"Unknown symbol: {symbol}")

    atomic_num = SYMBOLS[symbol]
    return f"{atomic_num}.{ion_stage:02d}"

def parse_symbol_and_ion(symbol_str: str) -> Tuple[str, int]:
    """
    Parse an element symbol and its ion stage from a string.

    The expected input format is "<Symbol> <IonStage>", where:
    - <Symbol> is a chemical symbol like 'Fe'.
    - <IonStage> can be either a Roman numeral in `ION_STAGES` (e.g., "I", "II", ...)
      or an integer (e.g., "2"). If absent, "I" (ion stage index 0) is used by default.

    This function returns a tuple of (symbol, ion_stage), where `ion_stage` is the
    index in the ION_STAGES list if the input is a recognized Roman numeral or the
    integer version if the input is numeric.

    Args:
        symbol_str (str): The input string containing the chemical symbol and ion stage.

    Returns:
        Tuple[str, int]: A tuple of (symbol, ion_stage_index).

    Raises:
        ValueError: If the ion stage is invalid (i.e., it’s not in ION_STAGES and
                    cannot be interpreted as an integer).
    """
    parts = symbol_str.strip().split()
    symbol = parts[0]
    ion_part = parts[1] if len(parts) > 1 else "I"

    if ion_part_is_decimal(ion_part):
        ion_stage = int(ion_part)
    elif ion_part in ION_STAGES:
        ion_stage = ION_STAGES.index(ion_part)
    else:
        raise ValueError(f"Invalid ion stage: {ion_part}")

    return symbol, ion_stage

def ion_part_is_decimal(ion_part: str) -> bool:
    """
    Check if a given string can be interpreted as an integer.

    Args:
        ion_part (str): String representing the ion stage, possibly in numeric form.

    Returns:
        bool: True if `ion_part` is a valid integer representation, False otherwise.
    """
    try:
        int(ion_part)
        return True
    except ValueError:
        return False
