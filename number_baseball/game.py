import os
import time

from .bot import Bot
from .history import History
from .utils import *


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

    def __init__(self, N=0, L=0, target=[], mode=0, history=None):
        """
        Initialize the Game object.

        Parameters:
        - N (int): Number of rounds in the game.
        - L (int): Length of the target number.
        - target (list): The target number to guess.
        - mode (int): The mode of the game (1: Alone, 2: Auto, 3: Compete).
        - history (History): The history of the game.
        """
        self.N = N
        self.L = L
        self.target = target
        self.mode = mode
        self.history = history
        self.is_set = False

    def start(self):
        """
        Starts the Number Baseball game.
        """
        os.system("clear")
        print("Welcome to Number Baseball!\n")

        show_rule = input("Show rule? (y/n) : ").lower()
        if show_rule == "y":
            self.show_rule()

        print()

        self.N = self.set_rounds()
        self.L = self.set_length()
        self.target = generate_numbers(self.L)
        self.mode = self.set_mode()
        self.is_set = True

        if self.mode == 1:
            self.history = self.play_alone()
        elif self.mode == 2:
            self.history = self.play_auto()
        elif self.mode == 3:
            self.history = self.play_compete()
        elif self.mode == 4:
            self.history = self.play_dual()
        else:
            print("Invalid mode!")

        print()
        self.history.show_history()
        print()

        self.is_set = False

        if input("Play again? (y/n) : ").lower() == "y":
            self.start()
            print()

    def show_rule(self):
        print('How to play number baseball game')
        print('- Goal: Guess the target number within the given number of rounds.')
        time.sleep(1)
        print('- Score: Home run, Strike, Ball, Out')
        time.sleep(1)
        print('  - Home run (HR): All numbers are correct and in the correct position. End the game.')
        time.sleep(1)
        print('  - Strike (S): The number is correct and in the correct position.')
        time.sleep(1)
        print('  - Ball (B): The number is correct but in the wrong position.')
        time.sleep(1)
        print('  - Out (O): No single number is correct.')
        time.sleep(3)
        print('- Example: Target number is 4 1 2')
        time.sleep(1)
        print('  - 5 6 7 -> O [No single number is correct]')
        time.sleep(1)
        print('  - 1 8 0 -> 0S 1B [1 is correct but in the wrong position]')
        time.sleep(1)
        print('  - 4 5 6 -> 1S 0B [4 is in the correct position]')
        time.sleep(1)
        print('  - 4 2 1 -> 2S [4 is in the correct position, 1 and 2 are correct but in the wrong position]')
        time.sleep(1)
        print('  - 4 1 2 -> Home run! [All numbers are correct and in the correct position]')
        time.sleep(3)
        print('- Modes: Alone, Auto, Compete, Dual')
        time.sleep(1)
        print('  - Alone: Play alone against the computer.')
        time.sleep(1)
        print('  - Auto: Watch the computer play against itself.')
        time.sleep(1)
        print('  - Compete: Play against the computer with in common target number.')
        time.sleep(1)
        print('  - Dual: Input your target number for computer and play against the computer.')
        time.sleep(3)
        print('- Have fun!')
        print()


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
        Prompts the user to input a mode (1: Alone, 2: Auto, 3: Compete, 4: dual) and returns the selected mode as an integer.

        Returns:
            int: The selected mode (1, 2, or 3).
        """
        mode = input("> Mode [1: Alone, 2: Auto, 3: Compete, 4: Dual] : ")
        if mode not in ["1", "2", "3", "4"]:
            print("Invalid input! Please input 1, 2, 3, or 4.")
            return self.set_mode()
        return int(mode)

    def play_alone(self):
        """
        Play the number baseball game alone.

        Returns:
            History: The history of the game.
        """
        assert self.is_set, 'Game is not set!'
        
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)
        history.set_mode(self.mode)

        for round in range(self.N):
            print(f"\nRound {round+1}")
            guess, tick = get_user_input(self.L)
            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score, tick)

            print(f'{" ".join(map(str, guess))} : {msg}')
            if is_end:
                print()
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
        assert self.is_set, 'Game is not set!'
        
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)
        history.set_mode(self.mode)

        bot = Bot(self.L)
        for round in range(self.N):
            print(f"\nRound {round+1}")
            guess, tick = bot.guess()
            print(f"> Input {self.L}-digit number: {' '.join(map(str, guess))}")
            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score, tick)
            bot.update(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg} ({len(bot)})')
            if is_end:
                print()
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
        assert self.is_set, 'Game is not set!'
        
        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)
        history.set_mode(self.mode)

        bot = Bot(self.L)
        for round in range(self.N):
            if round % 2 == 0:
                print(f"\nRound {round+1} (Bot's turn)")
                guess, tick = bot.guess()
                print(f"> Input {self.L}-digit number: {' '.join(map(str, guess))}")
            else:
                print(f"\nRound {round+1} (Your turn)")
                guess, tick = get_user_input(self.L)

            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score, tick)
            bot.update(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg} ({len(bot)})')
            if is_end:
                print()
                if round % 2 == 0:
                    print("Bot wins!")
                    history.set_winner("Bot")
                else:
                    print("You win!")
                    history.set_winner("User")
                break
        else:
            print("Draw!")

        return history
    
    def play_dual(self):
        assert self.is_set, 'Game is not set!'

        history = History()
        history.set_rounds(self.N)
        history.set_target(self.target)
        user_target, _ = get_user_input(self.L)
        history.set_user_target(user_target)
        history.set_mode(self.mode)

        bot = Bot(self.L)
        for round in range(self.N*2):
            print(f"\nRound {round+1} (Bot's turn)")
            guess, tick = bot.guess()
            print(f"> Input {self.L}-digit number: {' '.join(map(str, guess))}")
            score = get_score(user_target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score, tick)
            bot.update(guess, score)

            print(f'{" ".join(map(str, guess))} : {msg} ({len(bot)})')
            if is_end:
                print()
                print("Bot wins!")
                history.set_winner("Bot")
                break

            print(f"\nRound {round+1} (Your turn)")
            guess, tick = get_user_input(self.L)
            score = get_score(self.target, guess)
            msg, is_end = format_score(score, self.L)
            history.add_history(guess, score, tick)

            print(f'{" ".join(map(str, guess))} : {msg}')
            if is_end:
                print()
                print("You win!")
                history.set_winner("User")
                break
        
        else:
            print("Draw!")

        return history


