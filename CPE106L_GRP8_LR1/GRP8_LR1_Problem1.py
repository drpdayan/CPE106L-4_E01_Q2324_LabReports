import stats as sts

listinput = input("Enter a list of numbers: ")
intlist = list(map(int, listinput.split(" ")))

sts.mean(intlist)
sts.median(intlist)
sts.mode(intlist)

