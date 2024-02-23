from .utils import format_score


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
        self.mode = 0
        self.history = []

    def set_rounds(self, rounds):
        """
        Set the number of rounds.

        Parameters:
        - rounds (int): The number of rounds.
        """
        self.rounds = rounds

    def set_mode(self, mode):
        """
        Set the mode of the game.

        Parameters:
        - mode (int): The mode of the game (1: Alone, 2: Auto, 3: Compete).
        """
        self.mode = mode

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

    def add_history(self, guess, score, tick=0):
        """
        Add a guess and its score to the history.

        Parameters:
        - guess (list): The guess made by the player or bot.
        - score (tuple): The score of the guess.
        """
        self.history.append((guess, score, tick))

    def show_history(self):
        """
        Print the history of the game.
        """

        print("Game History:")
        print(f"- Rounds: {self.rounds}")
        print(f"- Target: {' '.join(map(str, self.target))}")
        print(f"- Winner: {self.winner}")
        print("- History:")
        for r_idx, (guess, score, tick) in enumerate(self.history, 1):
            msg, _ = format_score(score, len(self.target))
            if self.mode == 1:
                print(
                    f'  u{r_idx:02d}. {" ".join(map(str, guess))} : {msg:<10} - {tick:.2f} sec'
                )
            elif self.mode == 2:
                print(
                    f'  b{r_idx:02d}. {" ".join(map(str, guess))} : {msg:<10} - {tick:.2f} sec'
                )
            elif self.mode == 3:
                print(
                    f'  {"b" if r_idx%2 else "u"}{r_idx:02d}. {" ".join(map(str, guess))} : {msg:<10} - {tick:.2f} sec'
                )
            else:
                print(
                    f'  {r_idx:02d}. {" ".join(map(str, guess))} : {msg:<10} - {tick:.2f} sec'
                )
