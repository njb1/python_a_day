# src/hard.py


def is_disarium_number(num):
    """
    Determines if a given three-digit number is a Disarium number.
    A Disarium number is a number in which the sum of its digits powered to their 
    respective positions is equal to the number itself.
    For example, 175 is a Disarium number because 1^1 + 7^2 + 5^3 = 175.
    Parameters: num (int): A three-digit integer to check.
    Returns: bool: True if the number is a Disarium number, False otherwise.
    Raises: ValueError: If the input is not a three-digit number.
    """
    is_disarium = False

    if len(str(num)) != 3:
        raise ValueError("Input must be a three-digit number.")
    
    num = str(num)
    first = int(num[0])
    second = int(num[1])
    third = int(num[2])

    first_power = pow(first, 1)
    second_power = pow(second, 2)
    third_power = pow(third, 3)

    total = first_power + second_power + third_power

    if total == int(num):
        is_disarium = True
    else:
        is_disarium = False
    
    return is_disarium


def ginortS(s):
    """
    Sorts the input string such that all lowercase letters come first, 
    followed by uppercase letters, and then digits.
    Parameters: s (str): The input string to be sorted.
    Returns: str: A string with lowercase letters, then uppercase letters, 
    then digits, all in their original order.
    """
    lower = ""
    upper = ""
    odd = ""
    for i in s:
        if i.islower():
            lower += i
        elif i.isupper():
            upper += i
        elif i.isdigit():
            odd += i
    
    sorted_string = lower + upper + odd
    return sorted_string


def move_zeroes_to_end(n):
    """
    Moves all zeroes in the input number to the end of the number's string representation.
    Args: n (int or str): The input number or string containing digits.
    Returns: str: A string where all zeroes from the input are moved to the end, 
    preserving the order of non-zero digits.
    """
    n = str(n)
    count = 0
    new_string = ""
    for i in n:
        if i == "0":
            count += 1
        else:
            new_string += i
    
    new_string += "0" * count

    return new_string


def coin_change(coins, amount):
    sorted_coins = sorted(coins, reverse=True)
    result = 0
    for coin in sorted_coins:
        while amount >= coin:
            amount -= coin
            result += 1
        
    return result

