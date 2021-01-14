import string

import random


class Characters:
    def __init__(self, symbols, numbers):
        self.symbols = symbols
        self.numbers = numbers

    def capital_alpha(self):
        capital_letters = list(string.ascii_uppercase)
        return capital_letters

    def small_alpha(self):
        small_letters = list(string.ascii_lowercase)
        return small_letters

    def _numbers(self):
        numbers = self.numbers.split(" ")
        return numbers

    def _symbols(self):
        symbols = self.symbols.split(" ")
        return symbols


class Password:
    def generating_password(self):
        nums = " 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 "
        signs = "! @ # $ % ^ & * ( ) - _ = + ` ~ { } [ ] | \ : ; ' ? / > . < , "
        ch = Characters(signs, nums)
        capital_letters = ch.capital_alpha()
        small_letters = ch.small_alpha()
        numbers = ch._numbers()
        symbols = ch._symbols()
        characters = [capital_letters, small_letters, numbers, symbols]
        password = ""
        lengths = range(int(input("What should be the length of the password? ")))
        for length in lengths:
            index1 = int(random.uniform(0, 4))
            index2 = int(random.uniform(0, 26))
            character = characters[index1][index2]
            password += str(character)
        return password


def main():
    password = Password()
    return password.generating_password()
