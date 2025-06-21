"""
bot.py
~~~~~~

Contains all of the logic for the hangman bot.
The bot uses a regex to parse through the wordlist
and tries to determine which letter is the best
to guess.
"""

# pylint: disable=line-too-long

from __future__ import annotations

from typing import Iterable
from random import choice
import re

_MAIN_WORDLIST = "./src/words.txt"
_10000_WORDLIST = "./src/words10000.txt"
_ALPHABET = "abcdefghijklmnopqrstuvwxyz"



def read_wordlist(file: str):
    """
    Reads the wordlist file into a list.
    """
    with open(file, "r", encoding="utf-8") as f:
        words = f.read().strip().split('\n')

    return words


class LetterGuess:
    """
    A set of methods which determine the best letter to pick
    for a given hangman game state. `word_with_blanks`
    should be formatted using lowercase letters
    for correctly guessed letters
    and question marks (`'?'`) for unknown letters.\n
    Example: The secret word is 'hello' and the 'e'
    and 'o' are not yet guessed: `'h?ll?'`
    """
    def __init__(self, word_with_blanks: str, incorrectly_guessed_letters: str | Iterable[str],
                 wordlist_file: str=_MAIN_WORDLIST):

        self._wordlist = read_wordlist(wordlist_file)

        self.secret_word = word_with_blanks.lower()
        self.invalid_letters = [l.lower()
                                for l in incorrectly_guessed_letters]

        self.guessable_letters = "".join([l for l in _ALPHABET
                                          if l not in self.invalid_letters and l not in self.secret_word])

        self.valid_words = self.determine_possible_words()

        self.best_guess = ""
        self.best_guess_score = 0 # number of words containing the best guess
        self.determine_best_guess()


    def determine_possible_words(self):
        """
        Parses through a wordlist and determines which
        valid English words fit the current game state.
        """

        # Remove all invalid words
        valid_words = []
        # The '?' positions can contain any letter that was not already guessed.
        search_regex = self.secret_word.replace("?", f"[{self.guessable_letters}]")

        for word in self._wordlist:
            if re.fullmatch(search_regex, word):
                valid_words.append(word)

        return valid_words


    def determine_best_guess(self):
        """
        Determines which letter appears
        in the most valid words.
        """
        guess_candidates: dict[str, int] = {}

        for letter in self.guessable_letters:
            count = 0
            for word in self.valid_words:
                if letter in word:
                    count += list(word).count(letter)

            guess_candidates[letter] = count

        sorted_guesses = sorted(guess_candidates, key=guess_candidates.get, reverse=True)
        self.best_guess = sorted_guesses[0]
        self.best_guess_score = guess_candidates[self.best_guess]

        # Randomize equally strong guesses (to avoid predictability)
        equally_good_guesses = []
        for guess in sorted_guesses:
            if guess_candidates[guess] == self.best_guess_score:
                equally_good_guesses.append(guess)

        self.best_guess = choice(equally_good_guesses)
