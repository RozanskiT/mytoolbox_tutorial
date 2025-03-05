from typing import Union, Tuple

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

SYMBOLS = {symbol: num for num, symbol in ATOMIC_NUMBERS.items()}

ION_STAGES = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]


def kurucz_code_to_symbol(code: Union[float, str]) -> str:
    code_float = float(code)
    atomic_num = int(code_float)
    ion_stage = int(round((code_float - atomic_num) * 100))

    symbol = ATOMIC_NUMBERS.get(atomic_num, f"Z={atomic_num}")
    ion_str = ION_STAGES[ion_stage] if ion_stage < len(ION_STAGES) else f"IonStage={ion_stage}"
    return f"{symbol} {ion_str}"


def symbol_to_kurucz_code(symbol_str: str) -> str:
    symbol, ion_stage = parse_symbol_and_ion(symbol_str)

    if symbol not in SYMBOLS:
        raise ValueError(f"Unknown symbol: {symbol}")

    atomic_num = SYMBOLS[symbol]

    return f"{atomic_num}.{ion_stage:02d}"


def parse_symbol_and_ion(symbol_str: str) -> Tuple[str, int]:
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
    try:
        int(ion_part)
        return True
    except ValueError:
        return False
