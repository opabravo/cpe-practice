"""Diagram: https://i.imgur.com/ZEZ0alC.png"""


def count_bee(year: int):
    # Male -> 1 Male, 1 Female
    # Female -> 1 Male
    # Original Female is immortal
    previous_male_num = 0
    previous_female_num = 1
    for _ in range(year):
        male_num = previous_female_num * 1 + previous_male_num * 1
        female_num = previous_male_num * 1 + 1
        previous_male_num, previous_female_num = male_num, female_num
    print(f"{male_num} {male_num+female_num}")


while 1:
    year = int(input("Input Year: "))
    if year == -1:
        break
    count_bee(year)
