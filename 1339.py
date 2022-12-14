import string


def validate_str(text:str):
    assert len(text) < 100, "Plaintext must be less than 100 characters"
    assert all(char in string.ascii_uppercase for char in text), "Plaintext must only contain letters"

def do_check(str1:str, str2:str)->bool:
    validate_str(str1)
    validate_str(str2)

    mapper1 = {}
    mapper2 = {}
    for s in str1:
        if s not in mapper1:
            mapper1[s] = 1
        else:
            mapper1[s] += 1
    for s2 in str2:
        if s2 not in mapper2:
            mapper2[s2] = 1
        else:
            mapper2[s2] += 1
    # Check premature
    return sorted(mapper1.values()) == sorted(mapper2.values())


if __name__ == "__main__":
    result = []
    for _ in range(5):
        enc_text = input("Enter encrypted text: ")
        plain_text = input("Enter plaintext: ")
        #substitution_text = encrypt(plain_text)
        flag = do_check(plain_text, enc_text)
        if flag:
            result.append("Yes")
        else:
            result.append("No")
        print()


    for res in result:
        print(res)
