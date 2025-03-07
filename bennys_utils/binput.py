from typing import List, Optional, Union

def forceful_input(
    prompt: str,
    options: Optional[List[str]] = None,
    case_sensitive: bool = False,
    max_attempts: Optional[int] = None,
    raise_on_fail: bool = False
) -> Union[str, None]:
    """
    A forceful input function that ensures the user provides valid input.

    Args:
        prompt (str): The message displayed to the user.
        options (Optional[List[str]]): A list of valid choices. If None, any input is accepted.
        case_sensitive (bool): If False (default), input is compared case-insensitively.
        max_attempts (Optional[int]): The maximum number of attempts before failing. If None, loops forever.
        raise_on_fail (bool): If True, raises a ValueError after max_attempts is exceeded. Default is False.

    Returns:
        Union[str, None]: The valid user input, or None if max attempts are exceeded (unless raise_on_fail=True).
    
    Example:
        >>> forceful_input("Enter Y/N: ", ["y", "n"], max_attempts=3)
        (User has up to 3 attempts to enter a valid input)
    """
    attempts = 0

    while True:
        user_input = input(prompt).strip()
        attempts += 1

        if options:
            # Handle case sensitivity
            if not case_sensitive:
                user_input = user_input.lower()
                options = [opt.lower() for opt in options]

            if user_input in options:
                return user_input
            else:
                print(f"Invalid input! Please enter one of: {', '.join(options)}")

        else:
            # If no options are provided, accept any input
            return user_input

        # Check max attempts
        if max_attempts is not None and attempts >= max_attempts:
            print("Maximum attempts reached!")
            if raise_on_fail:
                raise ValueError("Too many invalid attempts!")
            return None  # Return None if max attempts are exceeded
