from typing import Union

class Money:
    """
    A simple class for formatting currency values.

    This class ensures that negative values are displayed as '-$100,000.00'
    instead of '$-100,000.00' and allows for different currency symbols.
    It also supports shortform notation (e.g., $10M instead of $10,000,000).

    Example Usage:
        >>> Money(100000)
        '$100,000.00'
        >>> Money(-100000)
        '-$100,000.00'
        >>> Money(5000000, "EUR", shortform=True)
        '€5M'
        >>> Money(-1250000, shortform=True)
        '-$1.25M'
    """

    def __init__(self, amount: Union[int, float], currency: str = "USD", shortform: bool = False):
        """
        Initializes the Money object with a numerical amount and currency symbol.

        Args:
            amount (int | float): The monetary value.
            currency (str, optional): The currency code (default: "USD").
            shortform (bool, optional): If True, outputs abbreviated notation (e.g., "$10M"). Default is False.
        """

        symbol_map = {
            "USD": "$",  # United States Dollar
            "EUR": "€",  # Euro
            "GBP": "£",  # British Pound
            "JPY": "¥",  # Japanese Yen
            "AUD": "A$", # Australian Dollar
            "CAD": "C$", # Canadian Dollar
            "CHF": "CHF", # Swiss Franc
            "CNY": "¥",  # Chinese Yuan
            "INR": "₹",  # Indian Rupee
        }

        self.amount = amount
        self.symbol = symbol_map.get(currency, currency)
        self.shortform = shortform 

    def __str__(self) -> str:
        """
        Returns the formatted currency string when the object is used in a print statement or f-string.

        Example:
            >>> str(Money(100000))
            '$100,000.00'
            >>> str(Money(-100000))
            '-$100,000.00'
            >>> str(Money(5000000, "EUR", shortform=True))
            '€5M'

        Returns:
            str: The formatted currency string.
        """
        if self.shortform:
            formatted_amount = self._shorten_number(self.amount)
        else:
            formatted_amount = f"{abs(self.amount):,.2f}"

        return f"-{self.symbol}{formatted_amount}" if self.amount < 0 else f"{self.symbol}{formatted_amount}"

    def __repr__(self) -> str:
        """
        Returns a developer-friendly representation of the Money object.

        Example:
            >>> repr(Money(1000))
            'Money(1000, $)'

        Returns:
            str: The string representation for debugging.
        """
        return f"Money({self.amount}, {self.symbol}, shortform={self.shortform})" if self.shortform else f"Money({self.amount}, {self.symbol})"

    def _shorten_number(self, value: float) -> str:
        """
        Converts large numbers into short notation (K, M, B).

        Args:
            value (float): The numerical value to format.

        Returns:
            str: The abbreviated currency format.
        """
        abs_value = abs(value)

        if abs_value >= 1_000_000_000:
            return f"{abs_value / 1_000_000_000:.2f}B"
        elif abs_value >= 1_000_000:
            return f"{abs_value / 1_000_000:.2f}M"
        elif abs_value >= 1_000:
            return f"{abs_value / 1_000:.2f}K"
        else:
            return f"{abs_value:.2f}"

