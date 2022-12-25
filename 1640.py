from collections import defaultdict


while 1:
    a, b = map(int, input("Enter Two Nums > ").split())
    digit_occurrs = defaultdict(int)
    if a == 0 and b == 0:
        break

    for num in range(a, b + 1):
        for i in range(10):
            digit_occurrs[i] += str(num).count(str(i))

    # Make 0 to be the first value in list
    sorted_result = " ".join([str(digit_occurrs[i]) for i in range(10)])
    print(sorted_result)
