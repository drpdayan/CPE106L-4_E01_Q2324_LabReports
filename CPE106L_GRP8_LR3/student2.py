"""
                CPE106L-E01_Grp8_4Q2324
File: student2.py
Code to create a program based on Programming Exercises 2. p.318
"""

#Imports Student class from student1.py module with the alias st
from student1 import Student as st 
#Imports random module with the alias rn
import random as rn


def main():

    student1 = st("Ken", 5)
    for i in range(1, 6):
        student1.setScore(i, 100) 

    student2 = st("Sophie", 5)
    for i in range(1, 6):
        student2.setScore(i, rn.randint(70,100))#Utilized the random function to set different grades on selected students

    student3 = st("Jerome", 5)
    for i in range(1, 6):
        student3.setScore(i, rn.randint(85,100))

    student4 = st("Mike", 5)
    for i in range(1, 6):
        student4.setScore(i, 100)

    student5 = st("Angela", 5)
    for i in range(1, 6):
        student5.setScore(i, rn.randint(75,100))
    
    #Creates a list for each Student instance
    studentlist = [student1, student2, student3, student4, student5]
    for student in studentlist: #Prints each instance in the list
        print(f"Student: {student.name} (Scores: {student.scores})") #uses f-string for better readability
    
    #Lambda function returns only the student name of the each element in the list
    #Sort method sorts each student name element
    studentlist.sort(key = lambda student: student.name)
    print("\n+++++++++Sorted List+++++++++ \n ")
    for i in studentlist:#Prints each sorted element in the list
        print(i)


if __name__ == "__main__":
    main()