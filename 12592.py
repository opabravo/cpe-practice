slogon_map = {}

group_count = int(input("Prince - slogon groups: "))
for _ in range(group_count):
    slogon_key = input("Slogon Key: ")
    slogon_value = input("Slogon Value: ")
    slogon_map[slogon_key] = slogon_value

question_count = int(input("Princess - Questions Count: "))
for _ in range(question_count):
    question = input("Question: ")
    print(slogon_map.get(question))

