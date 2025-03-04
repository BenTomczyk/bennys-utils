import pytest
from bennys_utils.formatting import Money

def test_standard_formatting():
    assert str(Money(1000)) == "$1,000.00"
    assert str(Money(-2500)) == "-$2,500.00"

def test_shortform_formatting():
    assert str(Money(1_500_000, shortform=True)) == "$1.50M"
    assert str(Money(-1_250_000, shortform=True)) == "-$1.25M"
    assert str(Money(500, shortform=True)) == "$500.00"

def test_repr():
    assert repr(Money(1000)) == "Money(1000, $)"
    assert repr(Money(1000, "EUR", shortform=True)) == "Money(1000, €, shortform=True)"

def test_currency():
    assert str(Money(1000, "EUR")) == "€1,000.00"
    assert str(Money(1000, "GBP")) == "£1,000.00"
    
if __name__ == "__main__":
    pytest.main()