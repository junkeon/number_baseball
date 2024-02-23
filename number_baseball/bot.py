import itertools
import math
import random
import time

from .utils import get_score

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

    def __init__(self, L, level=None):
        """
        Initialize the Bot class.

        Parameters:
        L (int): The length of the number to guess.
        level (int, optional): The level of the bot. Range 0(dum) - 1(smart). Defaults to 0.

        Returns:
        None
        """
        self.candis = self.init_candis(L)
        if level is None:
            self.level = self.set_level()

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

    def set_level(self):
        """
        Set the level of the bot.

        Returns:
        None
        """
        level = input("> Set the level of the bot [ 1: dum - 10: smart ] : ")
        if not level.isnumeric() or int(level) < 1 or int(level) > 10:
            print("Invalid input! Please input number between 1 and 10")
            return self.set_level()
        level = int(level)

        return level

    def guess(self):
        """
        Make a guess.

        Returns:
        int: The guessed number.
        """
        _tic = time.time()
        candi, score = self.candis[0]

        tic = random.random() * math.log(len(self.candis) + 1, score / 10 + 1.1)
        time.sleep(tic)

        if random.random() < 1 - self.level / 10:
            candi = random.choice(self.candis)[0]

        _toc = time.time()

        return candi, _toc - _tic

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
            else:
                if random.random() < 1 - self.level / 10:
                    tmp.append((candi, s))
        self.candis = sorted(tmp, key=lambda x: x[1], reverse=True)
