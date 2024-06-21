'''
This program
'''
txtfile = input("File Name: ")

f = open(txtfile, "r")

linenum = 0
chosenlinenum =  0
append_list = []
print ("\n" + "Mapua Alma Mater Per Line:" + "\n")

for line in f:
    linenum += 1
    print("{}: {}".format(linenum,line.strip()))
    append_list.append("{}: {}".format(linenum,line.strip()))

# print(append_list)

while True:
    chosenlinenum = int(input("Choose a line number:"))
    chosenlinenum -= 1
    
    print(append_list[chosenlinenum])

    if chosenlinenum == 0:
        print("Exit.")
        break

    



