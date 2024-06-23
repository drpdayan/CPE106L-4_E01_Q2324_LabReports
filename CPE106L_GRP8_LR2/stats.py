#/home/drpdayan/LocalRepo/SoftDes/Activities/CPE106L-4_E01_Q2324_LabReports/CPE106L_GRP8_LR2/statstxt.txt
def mean(fileName):
    f = open(fileName, 'r')
    numbers = []
    for line in f:
        words = line.split()
        for words in words:
            numbers.append(float(words))
    
    if not numbers:
        return 0
    
    else:
        mean = 0
        for i in numbers:
            mean += i
        
        mean /= len(numbers)
        return mean
    

def median(fileName):
    f = open(fileName, 'r')
    
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    if not numbers:
        return 0
    
    else:
        # Sort the list and print the number at its midpoint
        numbers.sort()
        midpoint = len(numbers) // 2
        # print("The median is", end=" ")
        if len(numbers) % 2 == 1:
            return(numbers[midpoint])
        else:
            return((numbers[midpoint] + numbers[midpoint - 1]) / 2)
            


def mode(fileName):
    f = open(fileName, 'r')
    
    # Input the text, convert its to words to uppercase, and
    # add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())
    
    if not words:
        return 0
    # Obtain the set of unique words and their
    # frequencies, saving these associations in
    # a dictionary
    else:
        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
            if number == None:
                # word entered for the first time
                theDictionary[word] = 1
            else:
                # word already seen, increment its number
                theDictionary[word] = number + 1

        # Find the mode by obtaining the maximum value
        # in the dictionary and determining its key
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key
                break

            
    
def main():
    fileName = input("Enter the file name: ")
    print("The median is", median(fileName))
    print("The mean is ", mean(fileName))
    print("The moode is", mode(fileName))

main()


#statstxt.txt
#2 3 4 5 6 7 8
