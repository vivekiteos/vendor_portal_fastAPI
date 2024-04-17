import random

def generate_random_issue_no():
    """
    Generate a random 6-digit number.

    Returns:
        int: Random 6-digit number.
    """
    return random.randint(100000, 999999)
