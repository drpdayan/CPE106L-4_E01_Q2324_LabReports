"""
                CPE106L-E01_Grp8_4Q2324
File: student.py
Resources to manage a student's name and test scores.
Updated the code to create a program based on Programming Exercises 1. p.318
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    #####
    #3 Methods in Student class created to cimpare students' names
    def equal(self, self2): #Method to test for equality
        return (self.name == self2.name)

    def lessthan(self, self2): #Method to test for less than
        return (self.name < self2.name)

    def greaterthanequal(self, self2): #Method to test for greater than
        return (self.name > self2.name)
    #####

def main():
    """A simple test."""

    #####
    student1 = Student("Ken", 5)
    print(student1)
    for i in range(1, 6):
        student1.setScore(i, 100) 
    print(student1)

    student2 = Student("Sophie", 5)
    for i in range(1, 6):
        student2.setScore(i, random.randint(70,100))#Utilized the random function to set different grades on selected students
    print(student2)

    student3 = Student ("Jerome", 5)
    for i in range(1, 6):
        student3.setScore(i, random.randint(85,100))
    print(student3)

    student4 = Student ("Mike", 5)
    for i in range(1, 6):
        student4.setScore(i, 100)
    print(student4)

    student5 = Student ("Angela", 5)
    for i in range(1, 6):
        student5.setScore(i, random.randint(75,100))
    print(student5)

    #Conditional Statements to check wheter each method 
    # correctly expresses the relationship of equality of each object
    #Calls each method on student1, passing student 3 as an argument
    if student1.equal(student3): #If return value of method is true then...
    
        print("Equal") 
    else:
        print("Not Equal") #Otherwise
    
    if student1.lessthan(student3):
        print("Less Than")
    
    if student1.greaterthanequal(student3):
        print("Greater Than or Equal")
    #####

if __name__ == "__main__":
    main()


