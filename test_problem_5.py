# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 5
# Description:

import os.path
import sys

from problem_5 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_4():
    if not os.path.exists("problem_5.py"):
        sys.exit("Error: problem_5.py not found")
    elif not os.path.exists("library_problem_5.py"):
        sys.exit("Error: library_problem_5.py not found.")

    expected_output = [
        "Digite quantos testes realizará: ",
        "Teste 1: ",
        "8 não é primo.",
        "Teste 2: ",
        "51 não é primo.",
        "Teste 3: ",
        "7 é primo."
    ]

    set_keyboard_input([3, 8, 51, 7])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
