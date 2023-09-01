# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 4
# Description:

import os.path
import sys

from problem_4 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_4():
    if not os.path.exists("problem_4.py"):
        sys.exit("Error: problem_4.py not found")
    elif not os.path.exists("library_problem_4.py"):
        sys.exit("Error: library_problem_4.py not found.")

    expected_output = [
        "Digite quantos testes realizará: ",
        "Teste 1: ",
        "6 é perfeito.",
        "Teste 2: ",
        "5 não é perfeito.",
        "Teste 3: ",
        "28 é perfeito."
    ]

    set_keyboard_input([3, 6, 5, 28])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
