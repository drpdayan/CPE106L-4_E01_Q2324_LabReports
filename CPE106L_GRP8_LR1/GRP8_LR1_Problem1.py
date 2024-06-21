import stats as sts

listinput = input("Enter a list of numbers: ")
intlist = list(map(int, listinput.split(" ")))

print(sts.mean(intlist))
print(sts.median(intlist))
print(sts.mode(intlist))

