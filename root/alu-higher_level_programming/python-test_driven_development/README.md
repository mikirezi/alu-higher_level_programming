# python-test_driven_development

This project introduces Test Driven Development (TDD) in Python using
doctest and unittest. Each function includes input validation, proper
docstrings, and thorough tests covering edge cases.

## Tasks

### 0. Integers addition
`0-add_integer.py` adds two integers, casting floats to integers first.

### 1. Divide a matrix
`2-matrix_divided.py` divides all elements of a matrix by a given number,
rounded to 2 decimal places.

### 2. Say my name
`3-say_my_name.py` prints `My name is <first_name> <last_name>`.

### 3. Print square
`4-print_square.py` prints a square of a given size using `#`.

### 4. Text indentation
`5-text_indentation.py` prints text with 2 new lines added after each
`.`, `?`, or `:`.

### 5. Max integer - Unittest
`6-max_integer.py` finds and returns the max integer in a list.
Unit tests are located in `tests/6-max_integer_test.py`.

## Usage

    python3 -m doctest -v ./tests/0-add_integer.txt
    python3 -m doctest -v ./tests/2-matrix_divided.txt
    python3 -m doctest -v ./tests/3-say_my_name.txt
    python3 -m doctest -v ./tests/4-print_square.txt
    python3 -m doctest -v ./tests/5-text_indentation.txt
    python3 -m unittest tests.6-max_integer_test

## Author
Guillaume
