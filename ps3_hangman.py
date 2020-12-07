# Hangman game

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    amountRight = 0 
    for i in secretWord:
        if i in lettersGuessed:
            amountRight += 1
            if amountRight == len(secretWord):
                return True

    if amountRight != len(secretWord):
        return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for i in secretWord:
        if i in lettersGuessed:
            word += i
        else:
            word += '_'
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    availableLetters = ''
    for i in alphabet:
        if i not in lettersGuessed:
            availableLetters += i
    return availableLetters

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordList = list(secretWord)
    length = len(secretWord)
    print 'Welcome to the game, Hangman!'
    print 'There is ',len(secretWord),' letters in the word.'
    i = 0
    guessList = []
    amountOfGuesses = 8
    filled = 0
    while isWordGuessed(secretWord,guessList) == False :
        print 'You have ', amountOfGuesses, ' guesses left.'
        print 'Available letters: ', getAvailableLetters(guessList)
        guess = raw_input('Please guess a letter: ')
        while guess in guessList:
            guess = raw_input("Please guess another letter that hasn't already been used: ")
        guessList.append(guess)
        board = getGuessedWord(secretWord,guessList)
        newFill = 0
        for i in board:
            if i is not '_':
                if filled == 0:
                    filled += 1
                else:
                    newFill += 1
        if newFill == filled:
            print 'Sorry! That letter is not in the word: ', board
            amountOfGuesses -= 1
            if amountOfGuesses == 0:
              break
        elif newFill > filled:
            print 'That is a good guess!: ', board
            filled = newFill

    if isWordGuessed(secretWord,guessList):
        print 'you did it! You guessed the right word!'
    else:
        print 'sorry fam you lose! The word is ',secretWord





secretWord = chooseWord(wordlist).lower()
hangman('c')
