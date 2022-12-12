import datetime


results = []
rounds = int(input("Please enter the number of rounds: "))
print()

for i in range(rounds):
    date_died = datetime.datetime.strptime(input("Please enter the day you died: "), "%d/%m/%Y")
    date_birth = datetime.datetime.strptime(input("Please enter your date of birth (DD/MM/YYYY): "), "%d/%m/%Y")
    print()
    age = date_died - date_birth
    if age.days < 0:
        results.append(f"Case ${i+1}: Invalid birth date.")
    elif age.days/365 >= 130:
        results.append(f"Case ${i+1}: Check birth date.")
    elif age == 0:
        results.append(f"Case ${i+1}: 0")
    else:
        results.append(f"Case ${i+1}: {int(age.days/365)}")


for result in results:
    print(result)

