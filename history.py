from utils import format_score


class History:
    """
    The History class represents the history of a number baseball game.

    Attributes:
    - rounds (int): The number of rounds played.
    - target (list): The target number.
    - winner (str): The name of the winner.
    - history (list): The history of guesses and scores made during the game.
    """

    def __init__(self):
        """
        Initialize the History object.
        """
        self.rounds = -1
        self.target = None
        self.winner = None
        self.history = []

    def set_rounds(self, rounds):
        """
        Set the number of rounds.

        Parameters:
        - rounds (int): The number of rounds.
        """
        self.rounds = rounds

    def set_target(self, target):
        """
        Set the target number.

        Parameters:
        - target (list): The target number.
        """
        self.target = target

    def set_winner(self, winner):
        """
        Set the winner of the game.

        Parameters:
        - winner (str): The name of the winner.
        """
        self.winner = winner

    def add_history(self, guess, score):
        """
        Add a guess and its score to the history.

        Parameters:
        - guess (list): The guess made by the player or bot.
        - score (tuple): The score of the guess.
        """
        self.history.append((guess, score))

    def print(self):
        """
        Print the history of the game.
        """
        print(f"- Rounds: {self.rounds}")
        print(f"- Target: {' '.join(map(str, self.target))}")
        print(f"- Winner: {self.winner}")
        print("- History:")
        for guess, score in self.history:
            msg, _ = format_score(score, len(self.target))
            print(f'  {" ".join(map(str, guess))} : {msg}')
