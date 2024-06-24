'''
This python file contains the functions needed 
For the LR1_Problem1 such as :
Mean, Median, Mode
'''

#Calculates the average (mean) on a given list of numbers
def mean(num):
    mean = 0
    for i in num: #For loops that adds all elements within a list
        mean += i
    mean /= len(num)
    return mean #Returns mean value


#Finds the median on a given list of numbers
def median(num):
    num.sort() #Sorts the list and finds its middle
    mid = len(num) // 2
    if len(num) % 2 == 1:
        median = (num[mid])
    else: #If the list contains an even number of elements
        median = ((num[mid] + num[mid - 1]) / 2)
    return median  #Returns median value


#Finds the mode on a given list of numbers
def mode(num):
    count = [] #Empty list to append each element with its frequency within the list
    for i in num:
        count.append(num.count(i))
    unique_count = []
    for i in count: #Stores unique counts
        if i not in unique_count:
            unique_count.append(i)
    if len(unique_count) > 1: #Conditional statement if there are multiple or no modes
        mx = []
        for i in list (range(len(count))):
            if count[i] == max (unique_count):
                mx.append(num[i])
        mode = [] # Appends potential modes (elements with max frequency)
        for i in mx:
            if i not in mode:
                mode.append(i)
        mode = int(mode[0]) #Transforms the return type from a list to an int
        return mode #Returns mode value


