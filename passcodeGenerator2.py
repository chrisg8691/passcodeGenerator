#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 05:15:45 2019

@author: chrisg8691
"""

import string
from secrets import choice

length = int(input('How long would you like your passcode to be? '))

chars = list(string.printable)
del chars[-6:]

passcode = []

while len(passcode) < length:
    passcode.append(choice(chars))
    
finalPasscode = ''.join([str(item) for item in passcode])
    
print(finalPasscode)