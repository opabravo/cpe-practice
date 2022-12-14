result = []
for _ in range(4):
    nums = input().split()
    a, b = int(nums[0]), int(nums[1])
    round_ = 1
    row = [a]
    while 1:
        x = a / (b ** round_)
        if not x.is_integer():
            break
        row.append(int(x))
        if int(x) == 1:
            break
        round_ += 1
    result.append(row)

for row in result:
    if row[-1] != 1:
        print("Boring!")
        continue
    print(' '.join([str(x) for x in row]))
