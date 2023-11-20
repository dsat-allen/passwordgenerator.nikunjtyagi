"""Python Password generator
Developed by Nikunj Tyagi"""

# Importing Modules
import os
from complex import *
from regular import *

print('='*100, end='\n')
print('Welcome To Password Generator!', end='\n')
print('='*100, end='\n\n')

print("""1. Generate Password Regular Mode (By Length).
2. Generate Password Complex Mode (By Characters).

""")

ch = int(input("Select your Choice (1 or 2) => "))

if ch==1:
    print("You Have Chosen Regular Mode !\n")
    length = int(input("Enter length of Password you want to Generate :- "))
    generatedPSWD = genPasswordList(length)
    print("Generated Password is :-", generatedPSWD)
    os.system('pause')

elif ch==2:
    print("You Have Chosen Complex Mode !\n")
    upperAlpha = int(input("Enter No. of Upper-case Letters to include (1-8) : "))
    lowerAlpha = int(input("Enter No. of Lower-case Letters to include (1-8) : "))
    specialChar = int(input("Enter No. of Special Characters to include (1-5) : "))
    num = int(input("Enter Numbers to include (1-8) : "))

    # Calling function from module complex.
    generatedPSWD = Password_Generator_Main(upperAlpha, lowerAlpha, specialChar, num)
    print("Generated Password is :-", generatedPSWD)
    os.system('pause')

else:
    print("Error!!!\nEnter only Valid Choice (1-2).")
    os.system('pause')


