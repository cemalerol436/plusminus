def plusMinus(arr):

    # To check 'n' number, does it comply with the condition.
    while int(n) <= 0 or int(n) > 100:
        return print("ops! Please Type a Number (from 1 to 100)")

    # Created lists to fill with the numbers in arr.
    positive_numbers = []
    negative_numbers = []
    zero_numbers = []
    arr = list(arr)

    # While loop to separate numbers and fill into list with append command.
    i = 0
    while i<n:
        i += 1
        while int(arr[i-1]) < -100 or int(arr[i-1]) > 100:      # To check 'arr' numbers, does it comply with the condition.
            return print("ops! Please a Type Number (from -100 to 100)")
        if arr[i-1] < 0:
           negative_numbers.append(arr[i-1])
        elif arr[i-1] > 0:
           positive_numbers.append(arr[i-1])
        else:
           zero_numbers.append(arr[i-1])

    # To illustrate numbers with 6 digits after decimal.
    total_positive = "{:.6f}".format((len(positive_numbers))/n)
    total_negative = "{:.6f}".format((len(negative_numbers))/n)
    total_zero = "{:.6f}".format((len(zero_numbers))/n)

    # Shows the results.
    print(total_positive)
    print(total_negative)
    print(total_zero)

if __name__ == '__main__':
    n = int(input("n:").strip())
    arr = map(int, input("arr:").rstrip().split())

plusMinus(arr)
