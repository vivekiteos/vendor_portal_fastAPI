import random

def generate_random_issue_no():
    """
    Generate a random 6-digit number.

    Returns:
        int: Random 6-digit number.
    """
    return random.randint(100000, 999999)


def generate_random_tracking_no():
    """
    Generate a random 6-digit number.

    Returns:
        int: Random 6-digit number.
    """
    return random.randint(1000000000, 9999999999)
