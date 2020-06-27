# Hangman game
#
# -----------------------------------

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    length = len(secretWord)
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count+=1
            
    return count == length


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for i in secretWord:
        if i in lettersGuessed:
            word = word + i
        else:
            word = word + ' _'
    
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string 
    word = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            word = word + i
            
    return word    

def game(guesses, lettersGuessed,secretWord):
    print("-------------")
    print("You have "+str(8 - guesses)+ " guesses left.")
    print("Available letters: "+ getAvailableLetters(lettersGuessed))
    guess = input("Please guess a letter: ")
    guess =  guess.lower()
    if guess in lettersGuessed:
        print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
    else:
        lettersGuessed.append(guess)
        if guess in secretWord:
            print("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
        else:
            guesses+=1
            print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessed))
    
    return lettersGuessed , guesses


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    totalguesses = 8 
    guesses = 0
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long.")
    
    
    while (not isWordGuessed(secretWord, lettersGuessed)) & (totalguesses - guesses > 0):
        lettersGuessed, guesses = game(guesses, lettersGuessed,secretWord)
    
        if isWordGuessed(secretWord, lettersGuessed):
            print("------------")
            print("Congratulations, you won!")
            break
        elif totalguesses - guesses ==0:
            print("------------")
            print("Sorry, you ran out of guesses. The word was "+secretWord+".")
            break
        else:
            continue




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
