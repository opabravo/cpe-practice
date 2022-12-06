"""
Topic: 11332 Summing Digits
Url: https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/11332.pdf
"""


def get_answer(num: str) -> int:
    """Return the sum that is less than 10"""
    splitted_nums = [int(x) for x in str(num)]
    if sum(splitted_nums) >= 10:
        new_num = sum(splitted_nums)
        return get_answer(new_num)
    return sum(splitted_nums)


if __name__ == "__main__":
    input_numbers = []
    while 1:
        user_input = input("Enter a number: ")
        if int(user_input) == 0:
            break
        input_numbers.append(user_input)

    for num in input_numbers:
        print(get_answer(num))
