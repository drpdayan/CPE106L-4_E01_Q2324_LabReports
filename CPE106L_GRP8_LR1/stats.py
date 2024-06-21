dan = [34, 69, 420, 1337, 420, 23, 80, 190, 2]

def mean(num):
    mean = 0
    for i in num:
        mean += i
    mean /= len(num)
    return mean


def median(num):
    num.sort()
    mid = len(num) // 2
    if len(num) % 2 == 1:
        median = (num[mid])
    else:
        median = (num[mid] + num[mid - 1] / 2)
    return median

def mode(num):
    count = []
    for i in num:
        count.append(num.count(i))
    unique_count = []
    for i in count:
        if i not in unique_count:
            unique_count.append(i)
    if len(unique_count) > 1:
        m = []
        for i in list (range(len(count))):
            if count[i] == max (unique_count):
                m.append(num[i])
        mode = []
        for i in m:
            if i not in mode:
                mode.append(i)
        return mode
    else:
        print("No Mode on the List")

print(mode(dan))