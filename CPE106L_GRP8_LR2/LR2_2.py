#/home/drpdayan/LocalRepo/SoftDes/Activities/CPE106L-4_E01_Q2324_LabReports/CPE106L_GRP8_LR2/lr2list.txt
filename = input("Input filename: ")

# Initializes list
words = []

# Opens txt file and puts the words in a list
f = open(filename, 'r')
words = f.readlines()
f.close()

# Strips line spaces
words = [i.strip() for i in words]

# Print all the words
for i in range(len(words)):
      print(words[i])
print("There are ", len(words), " lines on this text")
# User chooses line number to print
lineInput = 1
while lineInput != 0:
    lineInput = int(input("Enter line number (0 to exit): "))
    if lineInput < len(words) and lineInput > 0:
        print(words[lineInput - 1])