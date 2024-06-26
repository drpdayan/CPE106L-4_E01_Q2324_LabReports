'''
                    CPE106L-E01_Grp8_4Q2324
stat.py is similar to one of the programming exercises for LR1 wherein
The programs calculates the mean, median, and mode of a list
Instead of inputting the elements on a list*(From LR1), 
Users must input the text file that contains the said list
'''

#File name to be used: /home/drpdayan/LocalRepo/SoftDes/Activities/CPE106L-4_E01_Q2324_LabReports/CPE106L_GRP8_LR2/stats.txt

#Calculates the average (mean) on a given list of numbers
def mean(fileName):
    f = open(fileName, 'r')
    numbers = []
    for line in f:
        words = line.split()
        for words in words:
            numbers.append(float(words))
    
    #returns 0 if there is an empty list
    if not numbers:
        return 0
    
    else:
        mean = 0
        for i in numbers:
            mean += i
        
        mean /= len(numbers)
        return mean
    
#Finds the median on a given list of numbers
def median(fileName):
    f = open(fileName, 'r')
    
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    #returns 0 if there is an empty list
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
            

#Finds the mode on a given list of numbers
def mode(fileName):
    f = open(fileName, 'r')
    
    # Input the text, convert its to words to uppercase, and
    # add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())
    
    #returns 0 if there is an empty list
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
    #Input text file
    fileName = input("Enter the file name: ")
    #Prints the output based on each function
    print("The median is", median(fileName))
    print("The mean is ", mean(fileName))
    print("The mode is", mode(fileName))


if __name__ == "__main__":
    main()


