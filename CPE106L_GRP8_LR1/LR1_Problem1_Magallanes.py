'''
Magallanes input for Problem 1:
User will enter a list of numbers
The program will calculate and output
the mean, median, and mode, of the list
'''

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_num = sorted(numbers)
    n = len(sorted_num)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_num[mid - 1] + sorted_num[mid]) / 2
    else:
        return sorted_num[mid]

def mode(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

def user_input():
    while True:
        try:
            user_input = input("Enter a list of numbers: ")
            numbers = list(map(float, user_input.split()))
            if not numbers:
                raise ValueError("The list cannot be empty.")
            return numbers
        except ValueError as e:
            print(f"Invalid input: {e}.")

if __name__ == "__main__":
    numbers = user_input()
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))