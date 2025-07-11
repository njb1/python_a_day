# src/easy.py

pass_mark = 50

def can_enter_club(age = 0) -> bool:
    """
    Determines if a person is allowed to enter the club based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        bool: True if the person is 21 or older, False otherwise.
    """
    allowed = False
    if age >= 21:
        allowed = True
    return allowed


def pass_fail(score):
    if score >= pass_mark:
        return "Pass"
    else:
        return "Fail"

if __name__ == "__main__":
    print(pass_fail(pass_mark))

