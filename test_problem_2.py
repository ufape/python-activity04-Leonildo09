# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 2
# Description:

import os.path
import sys

from problem_2 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_2():
    if not os.path.exists("problem_2.py"):
        sys.exit("Error: problem_2.py not found.")
    elif not os.path.exists("library_problem_2.py"):
        sys.exit("Error: library_problem_2.py not found.")

    expected_output = [
        "=-=-=-=-=-=-=-=-=-=",
        "Digite o valor 1: ",
        "Digite o valor 2: ",
        "Os números são..: 12 13 17",
        "=-=-=-=-=-=-=-=-=-="
    ]

    set_keyboard_input([10, 18])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
