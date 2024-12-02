lint:
    @pylint . --exit-zero

testall:
    @pytest

test day:
    @pytest tests/test_{{day}}.py

run day:
    @python -m src.{{day}}

start day:
    @echo "Welcome to another day of Advent of Code!"
    @echo "Creating template files..."
    @touch inputs/{{day}}_example.txt
    @touch inputs/{{day}}_input.txt
    @sed 's/AOCDAYNAME/{{day}}/g' src/.template.py > src/{{day}}.py
    @sed 's/AOCDAYNAME/{{day}}/g' tests/.template.py > tests/test_{{day}}.py