# Python Minimal Module Tutorial – mytoolbox

This repository serves as a minimal example of a local Python package. It illustrates the basic structure and setup needed to quickly create and install a simple Python module.

## Python package how-to

### Directory structure

```plaintext
mytoolbox/
│
├── mytoolbox/
│   ├── __init__.py
│   └── kurucz_atomic_symbols.py
├── tests/
│   └── test_kurucz_atomic_symbols.py
├── pyproject.toml
└── README.txt
```

- `mytoolbox/__init__.py`:  
  Tells Python that `mytoolbox` is a package, allowing you to import its modules. Additionally, it serves as a convenient place to control how submodules are exposed to users. By importing specific functions into `__init__.py`, you simplify the API so users can directly access key functionalities without needing to know your module's internal structure. Alternatively, you could keep submodules separate, leaving it up to users to import each submodule explicitly. Both approaches have their merits: explicit submodules maintain clear boundaries, while convenience imports offer a simpler user experience.

- `mytoolbox/kurucz_atomic_symbols.py`:  
  Contains Python functions to convert between atomic symbols and Kurucz atomic codes.

- `tests/test_kurucz_atomic_symbols.py`:  
  Contains unit tests to verify the correctness of functions implemented in `kurucz_atomic_symbols.py`. Tests are optional but highly recommended, as they help you spot problems early and confidently modify your code without fear of unintentionally breaking existing functionality. While there's no need to put form over function, good tests ensure your module stays reliable and maintainable.

- `pyproject.toml`:  
  Tells Python how to install your module, including metadata and dependencies.

- `README.txt`:  
  Provides instructions and usage examples for your module. (You're reading this file right now!)

## Installation

Install locally in editable (`-e`) mode. You want to use this mode if you need to make changes to your code and immediately test them without reinstalling the package each time.
```bash
pip install -e .
```

## Running Tests (Optional)

Tests are provided for convenience to ensure the package functions correctly, but they are entirely optional when creating your package. To run all tests for this project:

Ensure you have pytest installed (if not already): 
```bash 
pip install pytest 
```

Navigate to the project’s root directory (the same directory containing pyproject.toml).
Run pytest: 
```bash 
pytest
``` 

For more detailed output, you can use: 
```bash
pytest -v
```

Pytest will automatically discover and execute any test files (like test_kurucz_atomic_symbols.py) located in the tests/ directory. If all is configured correctly, you should see a report indicating whether the tests passed or failed.

## Usage

After installation, the package can be imported and used as follows:
```python
import mytoolbox as mt

# Check the actual location of the imported module (helpful to understand effect of pip install -e)
print(mt.__file__)

# Print the docstring for the kurucz_code_to_symbol function
# help(mt.kurucz_code_to_symbol)

# Convert Kurucz code to atomic symbol and ion stage
print(mt.kurucz_code_to_symbol('26.01'))  # Output: Fe II

# Convert atomic symbol and ion stage to Kurucz code
print(mt.symbol_to_kurucz_code('Fe II'))  # Output: 26.01
```

### Interactive development with IPython

To automatically reload your module after editing the code:

```python
# Load IPython's autoreload extension and configure automatic reloading
%load_ext autoreload
%autoreload 2

# Import your module
import mytoolbox as mt

# Now, edits to 'kurucz_atomic_symbols.py' will automatically reload
print(mt.kurucz_code_to_symbol('26.01'))  # Immediate feedback from edits
```

## Clone and test locally

You can manually recreate this minimal module structure by following the directory structure provided above and creating each file yourself. However, if you prefer, you can quickly start by cloning the existing example using git:

```bash
git clone https://github.com/RozanskiT/mytoolbox_tutorial.git
cd mytoolbox_tutorial
```
Then proceed with installation steps above.