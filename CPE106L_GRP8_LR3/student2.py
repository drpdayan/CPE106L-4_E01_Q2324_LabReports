"""
File: student.py
Resources to manage a student's name and test scores.
"""
from student1 import Student as st
import random as rn

def main():

    names = []

    for i in range(1, 6):
        names.append(st("Student" + str(i), 5))
    
    rn.shuffle(names)

    print("Shuffled: ")
    for student in names:
        print(student)

    names.sort(key = lambda student: student.name)

    print("\nSorted: ")
    for student in names:
        print(student)

main()

