print("Enter Amount:", end=" ")
for _ in range(int(input())):
    m,y,c,s = input().split()
    m,y,c = int(m),int(y),int(c)
    
    for color in s:
        if(color == 'M'):
            m -= 1
        elif(color == 'Y'):
            y -= 1
        elif(color == 'C'):
            c -= 1
        elif(color == 'R'):
            m -= 1
            y -= 1
        elif(color == 'G'):
            y -= 1
            c -= 1
        elif(color == 'V'):
            m -= 1
            c -= 1
        elif(color == 'B'):
            m -= 1
            c -= 1
            y -= 1
    can_complete = 'YES' if (m>=0 and y>=0 and c>=0) else 'NO'
    result = f"{can_complete}"
    if(can_complete == 'YES'):
        result += f" {m} {y} {c}"
    print(result)