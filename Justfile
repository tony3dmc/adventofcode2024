lint:
    @pylint . --exit-zero

testall:
    @pytest

test day:
    @pytest tests/test_{{day}}.py

run day:
    @python -m src.{{day}}