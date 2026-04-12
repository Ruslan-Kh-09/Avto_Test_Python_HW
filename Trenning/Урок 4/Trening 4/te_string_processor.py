import pytest
from string_processor import StringProcessor

string_processor = StringProcessor()

@pytest.mark.parametrize(
    'input_text, output_text',
    [
        ("привет", "Привет."),
        ("Привет", "Привет."),
        ("", "."),
        ("Привет.", "Привет."),
    ],
)
def test_positive(input_text, output_text):

    assert string_processor.process(input_text) == output_text

@pytest.mark.parametrize(
    'input_text, output_text',
    [
        ("", "."),
        ("   ", "   ."),
        ("123asd", "123asd."),
        ("!@#$%^.", "!@#$%^."),
    ],
)
def test_negative(input_text, output_text):

    assert string_processor.process(input_text) == output_text

# def test_regular_string_without_dot():
#     """Тест на не пустую строку. Должна появиться заглавная буква."""
#     result = StringProcessor.process("привет")
#     assert result == "Привет."
#
# def test_regular_string_with_dot():
#     """Тест строку. Должна появиться заглавная буква."""
#     result = StringProcessor.process("привет.")
#     assert result == "Привет."
#
# def test_capital_string_without_dot():
#     """Тест не пустую строку. Должна появиться заглавная буква."""
#     result = StringProcessor.process("Привет")
#     assert result == "Привет."

# def test_string_with_one_letter():
#     """Тест не пустую строку. Должна появиться заглавная буква."""
#     result = StringProcessor.process("п")
#     assert result == "П."
#
# def test_string_with_numbers_and_symbols():
#     """Тест не пустую строку. Должна появиться заглавная буква."""
#     result = StringProcessor.process("123 фыва")
#     assert result == "123 фыва."
