# Hangman

import random

def main():
    word = randomWord()
    charList = wordToChars(word)
    listOfXs = displayXs(charList)
    characterGuess = userGuess()
    checkIfGuessIsCorrect(charList, characterGuess)
    

def randomWord():
    listOfWords = ["Game", "Throne", "Batman", "Books", "Football", "Movie", "Sword"]
    word = random.choice(listOfWords)
    print(word)
    return word

def wordToChars(word):
    charList = list(word)
    copyList = charList[:]
    listLength = len(charList)
    count = 0
    while count < listLength:
        char = charList[count]
        copyList[count] = char.lower()
        count = count + 1

    
    print(charList)
    return charList

def displayXs(charList):
    numberOfXs = len(charList)
    listOfXs = list(range(numberOfXs))
    count = 0
    while count < numberOfXs:
        listOfXs[count] = "X"
        count = count + 1
    print(listOfXs)
    return listOfXs

def userGuess():
    guess = input("Enter a letter: ")
    guessList = list(guess)
    if len(guessList) == 1:
        print("You entered a character")
        return guessList
    else:
        print("You did not enter a character")
        userGuess()

def checkIfGuessIsCorrect(charList, characterGuess):
    if characterGuess in charList:
        print("The guess is correct")
    else:
        print("The guess is incorrect")
main()