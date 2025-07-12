# src/easy.py

def can_enter_club(age = 0) -> bool:
    """
    Determines if a person is allowed to enter the club based on their age.
    Args: age (int): The age of the person.
    Returns: bool: True if the person is 21 or older, False otherwise.
    """
    allowed = False
    if age >= 21:
        allowed = True
    return allowed


def pass_fail(score, pass_mark=50) -> str:
    """
    Determines whether a given score meets the passing criteria.
    Args: score (int or float): The score to evaluate.
    Returns: str: "Pass" if the score is greater than or equal to pass_mark, otherwise "Fail".
    """
    if score >= pass_mark:
        return "Pass"
    else:
        return "Fail"


def is_divisible_by_five(n) -> bool:
    """
    Check if a number is divisible by five.
    Args: n (int): The number to check.
    Returns: bool: True if n is divisible by five, False otherwise.
    """
    if n % 5 == 0:
        return True
    else:
        return False
    

def replace_smiley(text):
    """
    Replaces all occurrences of the ':)' smiley in the input text with the '😊' emoji.
    Args: text (str): The input string in which to replace smileys.
    Returns: str: The modified string with ':)' replaced by '😊'.
    """
    edited_text = text.replace(":)", "😊")
    return edited_text


def convert_to_titlecase(s) -> str:
    """
    Converts a given string to title case.
    Args: s (str): The input string to be converted.
    Returns: str: The title-cased version of the input string.
    """
    title_string = s.title()
    return title_string

def number_to_dashes(n) -> str:
    """
    Converts a given integer into a string of dashes.
    Args: n (int): The number of dashes to include in the returned string.
    Returns: str: A string consisting of `n` consecutive dash ('-') characters.
    """
    dashed_string = ""
    for i in range(n):
        dashed_string += "-"
    return dashed_string

def add_ends(list_of_numbers) -> int:
    """
    Adds the first and last elements of a list of numbers.
    If the list is empty, returns 0.
    If the list contains only one element, returns double that element.
    Raises a TypeError if the input is not a list.
    Args: list_of_numbers (list): A list of numbers.
    Returns: int: The sum of the first and last elements, double the single element, or 0 for an empty list.
    Raises: TypeError: If the input is not a list.
    """
    if type(list_of_numbers) is not list:
        raise TypeError("Input must be a list.")
    elif not list_of_numbers or len(list_of_numbers) == 0:
        total = 0
    elif len(list_of_numbers) == 1:
        total = list_of_numbers[0] * 2
    else:
        first = list_of_numbers[0]
        last = list_of_numbers[-1]
        total = first + last
    return total


if __name__ == "__main__":
    print(add_ends([2, 4, 6]))  # Example usage

