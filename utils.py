import random


def generate_numbers(L=3):
    """
    Generate a list of random numbers.

    Parameters:
    L (int): The length of the generated list. Default is 3.

    Returns:
    list: A list of random numbers.
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:L]


def get_score(target, guess):
    """
    Calculates the score for a given guess in a number baseball game.

    Parameters:
    target (str): The target number to guess.
    guess (str): The guessed number.

    Returns:
    tuple: A tuple containing the number of strikes and balls.
    """
    s, b = 0, 0

    for idx, numb in enumerate(guess):
        if target[idx] == numb:
            s += 1
        elif numb in target:
            b += 1

    return s, b


def get_user_input(L):
    """
    Get user input for an L-digit number.

    Args:
        L (int): The number of digits in the input number.

    Returns:
        list: A list of integers representing the input number.

    Raises:
        None

    Examples:
        >>> get_user_input(3)
        > Input 3-digit number: 123
        [1, 2, 3]
    """
    guess = input(f"> Input {L}-digit number: ")

    if " " in guess:
        guess = guess.split()
    elif "," in guess:
        guess = guess.split(",")
    else:
        guess = list(guess)

    if len(guess) != L:
        print(f"Invalid input! Please input {L}-digit number.")
        return get_user_input(L)

    if not all(map(str.isnumeric, guess)):
        print("Invalid input! Please input number.")
        return get_user_input(L)

    if len(set(guess)) != L:
        print("Invalid input! Please input distinct number.")
        return get_user_input(L)

    return list(map(int, guess))


def format_score(score, L):
    """
    Formats the score of a number baseball game.

    Args:
        score (tuple): A tuple containing the number of strikes (s) and balls (b).
        L (int): The length of the target number.

    Returns:
        str: The formatted score string.
        bool: True if it's a home run, False otherwise.
    """
    s, b = score

    if s + b == 0:
        return "OUT", False
    elif s == L:
        return "Home run!", True
    else:
        return f"{s}S {b}B", False
