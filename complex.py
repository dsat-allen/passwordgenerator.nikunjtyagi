"""Advanced Password Generator"""

# Importing Random Module.
import random as rd

# Creating Lists for all required Characters.
upperAlpha = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S','T',
                'U', 'V', 'W', 'X', 'Y', 
                'Z']

lowerAlpha = ['a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y',
                'z']

specialCharacters = ['!', '@', '#', '$' ,'&']

numList = ['0', '1', '2', '3', '4', 
            '5', '6', '7', '8', '9']


def generate_Random_List(digitUA, digitLA, digitSC, digitNUM):
    # Creating Empty list to accomodate generated lists of characters.
    genUA=[]
    genLA=[]
    genNum=[]
    genSC=[]

    # Generating Upper Case List using Random Module.
    for i in range(1, digitUA+1):
        randomUA = rd.choice(upperAlpha)
        genUA.append(randomUA)

    # Generating Lower Case List using Random Module.
    for i in range(1, digitLA+1):
        randomLA = rd.choice(lowerAlpha)
        genLA.append(randomLA)

    # Generating Special Characters List using Random Module.
    for i in range(1, digitSC+1):
        randomSC = rd.choice(specialCharacters)
        genSC.append(randomSC)

    # Generating Numbers List using Random Module.
    for i in range(1, digitNUM+1):
        randomNUM = str(rd.randrange(1,9))
        genNum.append(randomNUM)

    genList = genUA + genLA + genSC + genNum
    rd.shuffle(genList)              # Shuffling genList to get more Complex Password.

    return genList

def list_To_String(output_shuffled):
    """Function to convert generated list to String Type."""
    output=''
    for i in output_shuffled:
        output = output+i

    return output

def Password_Generator_Main(digitUA, digitLA, digitSC, digitNUM):
    """Main function that will interact with Main Python File.
    Will Generate Complex Password."""

    # Calling generate_Random_List() Function.
    outputList = generate_Random_List(digitUA, digitLA, digitSC, digitNUM)

    # Calling list_To_String() Function to convert List into String.
    
    return list_To_String(outputList)





