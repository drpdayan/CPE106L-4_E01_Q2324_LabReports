'''
This program asks users to open a text file and read it
Each line is appended with a number according to its positsion
Users can choose any number that represents any line
If users choose 0, the program will close 
'''

#Prompts user to input file name
#Example Text File : "MapuaAlmaMater.txt"
txtfile = input("File Name: ")

#Programs opens and reads the text file"
f = open(txtfile, "r")


#Declaration of Variables
linenum = 0
chosenlinenum =  0
append_list = []

# The program prints the text file alongside its corresponding number per line
print ("\n" + "Mapua Alma Mater Per Line:" + "\n")
for line in f:
    linenum += 1
    print("{}: {}".format(linenum,line.strip()))
    append_list.append("{}: {}".format(linenum,line.strip())) # Each line is then appended on an empty 
                                                              # list where its index can be used to pick any line

# print(append_list)

#A while loop statement is used to choose a line number
while True:
    chosenlinenum = int(input("Choose a line number:"))
    chosenlinenum -= 1 #List index starts with 0
    
    
    print(append_list[chosenlinenum]) #The chosen line number is then displayed 

    if chosenlinenum == 0: #When "0" is chosen, the program exits
        print("Exit.")
        break

    



