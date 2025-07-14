# src/medium.py

from datetime import datetime


def mask_credit_card(card_number) -> str:
    """
    Masks all but the last four digits of a credit card number.
    Args: card_number (str): The credit card number as a string.
    Returns: str: The masked credit card number, with all but the last four digits replaced by asterisks.
    Raises: ValueError: If the credit card number is less than or equal to 4 digits long.
    """
    card_number = card_number.replace("-", "")  # Remove dashes if present
    if len(card_number) <= 4:
        raise ValueError("Credit card number must be at least 4 digits long.")
    else:
        last_four_digits = card_number[-4:]
        masked_part = '*' * (len(card_number) - 4)
        masked_plus_last_four_digits = masked_part + last_four_digits
        return masked_plus_last_four_digits


def is_pronic(n) -> bool:
    """
    Check if a given number is a pronic number.
    A pronic number is a number which is the product of two consecutive integers,
    that is, n = x * (x + 1) for some integer x.
    Args: n (int): The number to check.
    Returns: bool: True if n is a pronic number, False otherwise.
    """
    for i in range(n):
        if i * (i + 1) == n:
            return True
    return False

def can_type(keys, word) -> bool:
    """
    Determines if a given word can be typed using the provided set of keys.
    Args: keys (iterable): An iterable containing the available keys (characters).
        word (str): The word to check for typeability.
    Returns: bool: True if all characters in the word are present in keys, False otherwise.
    """
    can_type = True
    for i in word:
        if i not in keys:
            return False
    return can_type


def to_spongecase(text):
    """
    Converts the input text to "spongecase" where characters at even indices are lowercase
    and characters at odd indices are uppercase.
    Args: text (str): The input string to be converted.
    Returns: str: The converted string in spongecase format.
    """
    converted_text = ""
    for i in range(len(text)):
        if i % 2 == 0:
            converted_text += text[i].lower()
        else:
            converted_text += text[i].upper()

    return converted_text


def is_friday_13(month, year):
    """
    Determines if the 13th day of a given month and year falls on a Friday.
    Args: month (int): The month as an integer (1-12).
        year (int): The year as a four-digit integer.
    Returns: bool: True if the 13th is a Friday, False otherwise.
    """
    is_friday_13 = False
    date = datetime(year, month, 13)
    if date.weekday() == 4:  # 4 corresponds to Friday
        is_friday_13 = True
    else:
        is_friday_13 = False
    return is_friday_13


def harmonic_sum(n):
    """
    Calculate the nth harmonic sum.
    The harmonic sum is defined as the sum of the reciprocals of the first n natural numbers:
        H(n) = 1 + 1/2 + 1/3 + ... + 1/n
    Args:
        n (int): The number of terms in the harmonic sum.
    Returns:
        float: The harmonic sum rounded to two decimal places.
    """
    sum = 0
    for i in range(1, n + 1):
        if i == 1:
            sum = 1
        else:
            sum += 1 / i
    return round(sum, 2)
    