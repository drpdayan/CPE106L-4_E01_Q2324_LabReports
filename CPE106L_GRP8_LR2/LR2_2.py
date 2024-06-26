'''
                   CPE106L-E01_Grp8_4Q2324
LR2_2.py is similar to a programming excercise on LR1 where
User input a text file, the program opens and converts each line
Into and element on a list. It well then print the text file and
Tell how many lines there are on a text
User will then input a number to show the corresponding line
0 exits the program
'''

#/home/drpdayan/LocalRepo/SoftDes/Activities/CPE106L-4_E01_Q2324_LabReports/CPE106L_GRP8_LR2/MapuaAlmaMater.txt
filename = input("Input filename: ")

# Initializes list
words = []

# Opens txt file and puts the lines in a list
f = open(filename, 'r')
words = f.readlines()
f.close()

# Strips line spaces
words = [i.strip() for i in words]

# Print all the words
for i in range(len(words)):
      print(words[i])
print("\nThere are ", len(words), " lines on this text")

# User chooses line number to print
lineInput = 1
while lineInput != 0:
    lineInput = int(input("\nEnter line number (0 to exit): "))
    if lineInput < len(words) and lineInput > 0:
        print(words[lineInput - 1])

    else:
        print("Program End.")
        break

