# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 3
# Description:

import os.path
import sys

from problem_3 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_3():
    if not os.path.exists("problem_3.py"):
        sys.exit("Error: problem_3.py not found")
    elif not os.path.exists("library_problem_3.py"):
        sys.exit("Error: library_problem_3.py not found.")

    expected_output = [
        "=-=-=-=-=-=-=-=-=-=",
        "Digite o valor inicial: ",
        "A soma dos 5 pares é..: 40",
        "Digite o valor inicial: ",
        "A soma dos 5 pares é..: 80",
        "Digite o valor inicial: ",
        "=-=-=-=-=-=-=-=-=-="
    ]

    set_keyboard_input([4, 11, 0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
