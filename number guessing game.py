# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:03:33 2024
"""

import random

n = random.randrange(1, 10)
guess = int(input("Please Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right")

