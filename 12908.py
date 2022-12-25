while 1:
    bad_count = int(input(">"))
    if bad_count == 0:
        continue

    total = 0
    for i in range(1, 10**8):
        total += i
        if total > bad_count:
            print(total - bad_count, i)
            break