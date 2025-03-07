import pytest
from unittest.mock import patch
from bennys_utils.binput import forceful_input

# Test normal input (no restrictions)
@patch("builtins.input", side_effect=["Hello"])
def test_forceful_input_any_input(mock_input):
    result = forceful_input("Enter something: ")
    assert result == "Hello"

# Test input with valid options
@patch("builtins.input", side_effect=["wrong", "no", "yes"])  # 1st invalid, 2nd valid
def test_forceful_input_with_options(mock_input):
    result = forceful_input("Enter yes/no: ", ["yes", "no"])
    assert result == "no"

# Test case-insensitive matching
@patch("builtins.input", side_effect=["YeS"])
def test_forceful_input_case_insensitive(mock_input):
    result = forceful_input("Enter yes: ", ["yes"], case_sensitive=False)
    assert result == "yes"  # Should match lowercase "yes"

# Test case-sensitive matching
@patch("builtins.input", side_effect=["yes", "Yes"])  # First invalid due to case
def test_forceful_input_case_sensitive(mock_input):
    result = forceful_input("Enter Yes: ", ["Yes"], case_sensitive=True)
    assert result == "Yes"  # Second input matches exactly

# Test max_attempts (stops and returns None)
@patch("builtins.input", side_effect=["wrong", "invalid"])
def test_forceful_input_max_attempts(mock_input):
    result = forceful_input("Enter yes/no: ", ["yes", "no"], max_attempts=2)
    assert result is None  # Should return None after 2 failed attempts

# Test max_attempts with raise_on_fail=True (raises ValueError)
@patch("builtins.input", side_effect=["wrong", "invalid"])
def test_forceful_input_max_attempts_raises(mock_input):
    with pytest.raises(ValueError, match="Too many invalid attempts!"):
        forceful_input("Enter yes/no: ", ["yes", "no"], max_attempts=2, raise_on_fail=True)

# Test input with only valid options (no looping needed)
@patch("builtins.input", side_effect=["yes"])
def test_forceful_input_first_try(mock_input):
    result = forceful_input("Enter yes: ", ["yes", "no"])
    assert result == "yes"

