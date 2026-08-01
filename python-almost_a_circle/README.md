# python-almost_a_circle

This project implements a small class hierarchy (`Base`, `Rectangle`,
`Square`) with attribute validation, serialization to/from JSON, and
full unit test coverage, following the "Almost a Circle" curriculum.

## Structure

- `models/base.py` — the `Base` class, managing `id` and JSON
  serialization helpers (`to_json_string`, `from_json_string`,
  `save_to_file`, `load_from_file`, `create`).
- `models/rectangle.py` — the `Rectangle` class, inherits from `Base`.
- `models/square.py` — the `Square` class, inherits from `Rectangle`.
- `tests/test_models/` — unit tests for all classes.

## Usage

    python3 -m unittest discover tests

## Author
Guillaume
