"""Regular Python Password Generator"""
import random as rd 

# Importing Lists from complex Module.
from complex import upperAlpha, lowerAlpha, specialCharacters, numList, list_To_String

genList = []
fullList = upperAlpha + lowerAlpha + specialCharacters + numList

# Defining function to generated password.
def genPasswordList(length):
    """Generate Random Password based on length only."""
    for i in range(1, length+1):
        randomChoice = rd.choice(fullList)
        genList.append(randomChoice)

    return list_To_String(genList)

