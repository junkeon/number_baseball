from bot import Bot

from utils import *

from history import History


class Game:
    """
    Represents a number baseball game.

    Attributes:
    - N (int): Number of rounds in the game.
    - L (int): Length of the target number.
    - target (list): The target number to guess.
    - mode (int): The mode of the game (1: Alone, 2: Auto, 3: Compete).
    - history (History): The history of the game.

    Methods:
    - set_rounds(): Sets the number of rounds in the game.
    - set_length(): Sets the length of the target number.
    - set_mode(): Sets the mode of the game.
    - play_alone(): Plays the game in Alone mode.
    - play_auto(): Plays the game in Auto mode.
    - play_compete(): Plays the game in Compete mode.
    """

    def __init__(self):
        self.N = self.set_rounds()
        self.L = self.set_length()
        self.target = generate_numbers(self.L)
        self.mode = self.set_mode()

        if self.mode == 1:
            self.history = self.play_alone()
        elif self.mode == 2:
            self.history = self.play_auto()
        elif self.mode == 3:
            self.history = self.play_compete()
        else:
            print("Invalid mode!")

    def set_rounds(self):
        """
        Sets the number of rounds for the game.

        Returns:
            int: The number of rounds.
        """
        rounds = input("> Number of rounds : ")
        if not rounds.isnumeric():
            print("Invalid input! Please input number.")
            return self.set_rounds()
        return int(rounds)

    def set_length(self):
        """
        Set the length of the number.

        Returns:
            int: The length of the number.
        """
        length = input("> Length of number : ")
        if not length.isnumeric():
            print("Invalid input! Please input number.")
            return self.set_length()
        if int(length) > 10:
            print("Invalid input! Please input number less than 10.")
            return self.set_length()
        if int(length) < 1:
            print("Invalid input! Please input number more than 1.")
            return self.set_length()
        return int(length)

    def set_mode(self):
        """
        Prompts the user to input a mode (1: Alone, 2: Auto, 3: Compete) and returns the selected mode as an integer.

        Returns:
            int: The selected mode (1, 2, or 3).
        """
        mode = input("> Mode (1: Alone, 2: Auto, 3: Compete) : ")
        if mode not in ["1", "2", "3"]:
            print("Invalid input! Please input 1, 2, or 3.")
            return self.set_mode()
        return int(mode)

    def play_alone(self):
        """
        Play the number baseball game alone.

        Returns:
            History: The history of the game.
        """
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)

        for round in range(self.N):
            print(f"\nRound {round+1}")
            guess = get_user_input(self.L)
            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg}')
            if is_end:
                print("You win!")
                history.set_winner("User")
                break
        else:
            print("You lose!")

        return history

    def play_auto(self):
        """
        Play an automated game of number baseball.

        Returns:
            history (History): The history of the game.
        """
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)

        bot = Bot(self.L)
        for round in range(self.N):
            print(f"\nRound {round+1}")
            guess = bot.guess()
            print(f"> Input {self.L}-digit number: {' '.join(map(str, guess))}")
            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score)
            bot.update(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg} ({len(bot)})')
            if is_end:
                print("Bot wins!")
                history.set_winner("Bot")
                break
        else:
            print("Bot loses!")

        return history

    def play_compete(self):
        """
        Play a competitive game of number baseball.

        Returns:
            history (History): The history of the game.
        """
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)

        bot = Bot(self.L)
        for round in range(self.N):

            if round % 2 == 0:
                print(f"\nRound {round+1} (Bot's turn)")
                print(f"> Input {self.L}-digit number: {' '.join(map(str, guess))}")
                guess = bot.guess()
            else:
                print(f"\nRound {round+1} (Your turn)")
                guess = get_user_input(self.L)

            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score)
            bot.update(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg} ({len(bot)})')
            if is_end:
                if round % 2 == 0:
                    print("Bot wins!")
                    history.set_winner("Bot")
                else:
                    print("You win!")
                    history.set_winner("User")
                break
        else:
            print("Draw!")

        history.print()
        return history
