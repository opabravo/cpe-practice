def check_sum_is_2(nums: list):
    """Check if sum==2"""
    return sum(nums) == 2


def get_splitted_num(num:str):
    return [int(x) for x in str(num)]


def get_answer(num: str):
    splitted_nums = get_splitted_num(num)
    if sum(splitted_nums)>=10:
        num = sum(splitted_nums)
        return get_answer(num)
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
