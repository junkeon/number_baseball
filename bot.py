import itertools
import random
import time

from utils import get_score

INIT_SCORE = 1000


class Bot:
    """
    A class representing a bot for playing number baseball.

    Attributes:
    - candis (list): The list of candidates.

    Methods:
    - __init__(self, L): Initialize the Bot class.
    - __len__(self) -> int: Get the number of candidates.
    - init_candis(self, L): Initialize the list of candidates.
    - guess(self) -> int: Make a guess.
    - update(self, guess, score): Update the list of candidates based on the guess and score.
    """

    def __init__(self, L):
        """
        Initialize the Bot class.

        Parameters:
        L (int): The length of the number to guess.

        Returns:
        None
        """
        self.candis = self.init_candis(L)

    def __len__(self) -> int:
        """
        Get the number of candidates.

        Returns:
        int: The number of candidates.
        """
        return len(self.candis)

    def init_candis(self, L):
        """
        Initialize the list of candidates.

        Parameters:
        L (int): The length of the number to guess.

        Returns:
        list: The list of candidates.
        """
        return [(candi, INIT_SCORE) for candi in itertools.permutations(range(10), L)]

    def guess(self):
        """
        Make a guess.

        Returns:
        int: The guessed number.
        """
        tic = random.random()
        time.sleep(tic)
        return self.candis[0][0]

    def update(self, guess, score):
        """
        Update the list of candidates based on the guess and score.

        Parameters:
        guess (int): The guessed number.
        score (tuple): The score received for the guess.

        Returns:
        None
        """

        def add_score(score):
            s, b, *_ = score
            return s * 10 + b

        tmp = []
        for candi, s in self.candis:
            if get_score(candi, guess) == score:
                if any(n1 == n2 for n1, n2 in zip(candi, guess)):
                    if s == INIT_SCORE:
                        s = 0
                    s += add_score(score)
                tmp.append((candi, s))
        self.candis = sorted(tmp, key=lambda x: x[1], reverse=True)
