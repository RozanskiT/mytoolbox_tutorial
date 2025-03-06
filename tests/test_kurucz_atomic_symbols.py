import pytest
from mytoolbox import (
    kurucz_code_to_symbol,
    symbol_to_kurucz_code
)

def test_kurucz_code_to_symbol_fe_ii():
    """
    Test that the Kurucz code '26.01' properly translates to 'Fe II'.
    """
    result = kurucz_code_to_symbol('26.01')
    assert result == 'Fe II', f"Expected 'Fe II', got {result}"

def test_symbol_to_kurucz_code_fe_ii():
    """
    Test that the symbol 'Fe II' properly translates back to the code '26.01'.
    """
    result = symbol_to_kurucz_code('Fe II')
    assert result == '26.01', f"Expected '26.01', got {result}"
