"""
                    CPE106L-E01_GRP8_4Q2324
Program: generator.py
Author: Ken , Modified by GRP8
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

################################
#File names
noun = "nouns.txt"
verb = "verbs.txt"
art = "articles.txt"
preposition = "prepositions.txt"

#Function that gets the words on text files
def getWords(fname):
    f = open(fname, "r")
    words_list = []

    #Appends text files on a list
    for line in f:
        words_list.append(line.strip())

    f.close

    #Converts list into tuple
    words_tuple = tuple(words_list)

    return words_tuple


nouns = getWords(noun)
verbs = getWords(verb)
articles = getWords(art)
prepositions = getWords(preposition)

# #Prints functions to check
# print (articles)
# print (nouns)
# print (prepositions)
# print (verbs)
################################



def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
