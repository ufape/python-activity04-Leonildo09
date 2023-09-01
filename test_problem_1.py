# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Description:

import os.path
import sys

from problem_1 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_1():
    if not os.path.exists("problem_1.py"):
        sys.exit("Error: problem_1.py not found.")
    elif not os.path.exists("library_problem_1.py"):
        sys.exit("Error: library_problem_1.py not found.")

    expected_output = [
        "=-=-=-=-=-=-=-=-=-=",
        "Digite a nota 1: ",
        "Digite a nota 2: ",
        "Digite a nota 3: ",
        "Digite a nota 4: ",
        "Media: 5.4",
        "Aluno em exame.",
        "Digite a nota do exame: ",
        "Aluno aprovado.",
        "Media final: 5.9",
        "=-=-=-=-=-=-=-=-=-="
    ]

    set_keyboard_input([2.0, 4.0, 7.5, 8.0, 6.4])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"

    expected_output = [
        "=-=-=-=-=-=-=-=-=-=",
        "Digite a nota 1: ",
        "Digite a nota 2: ",
        "Digite a nota 3: ",
        "Digite a nota 4: ",
        "Media: 4.8",
        "Aluno reprovado.",
        "=-=-=-=-=-=-=-=-=-="
    ]

    set_keyboard_input([2.0, 6.5, 4.0, 9.0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"

    expected_output = [
        "=-=-=-=-=-=-=-=-=-=",
        "Digite a nota 1: ",
        "Digite a nota 2: ",
        "Digite a nota 3: ",
        "Digite a nota 4: ",
        "Media: 7.3",
        "Aluno aprovado.",
        "=-=-=-=-=-=-=-=-=-="
    ]

    set_keyboard_input([9.0, 4.0, 8.5, 9.0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
