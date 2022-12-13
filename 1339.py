import string
import itertools


WORDS = string.ascii_uppercase


def check_sub(original_str:str, str2:str):
    """Check if a plaintext string is a subsitution of a ciphertext string"""
    assert len(original_str) < 100, "Plaintext must be less than 100 characters"
    assert all(char in WORDS for char in original_str), "Plaintext must only contain letters"

    mapper = dict(zip(original_str, str2))
    # 檢查是否符合一對一的條件, 錯誤Ex: A -> B, A -> C
    print(mapper)
    return len(set(mapper.values())) == len(set(mapper.keys()))
    # result_str = "".join(mapper[char] for char in original_str)
    # return result_str == str2

    # return "".join(WORDS[(WORDS.index(char) + 1) % 26] for char in plaintext)


def check_premutation(str1:str, str2:str) -> bool:
    """Check if a plaintext string is a premutation of a ciphertext string"""
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


result = []
for _ in range(5):
    enc_text = input("Enter encrypted text: ")
    plain_text = input("Enter plaintext: ")
    #substitution_text = encrypt(plain_text)
    is_permutation = check_premutation(plain_text, enc_text)
    if is_permutation:
        result.append("YES")
        continue
    else:
        permutations = itertools.permutations(plain_text)
        for perm in permutations:
            print(''.join(perm))
            if check_sub(''.join(perm), enc_text):
                result.append("YES")
                break
    if check_sub(plain_text, enc_text):
        result.append("YES")
        continue
    result.append("NO")
    print()


for res in result:
    print(res)
