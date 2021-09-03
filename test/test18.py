with open('data/chicken.txt','r') as chicken:
    total = 0
    total_days = 0
    for i in chicken:
        data = i.strip()
        money = data.split(': ')
        total += int(money[1])
        total_days += 1
    print(total/total_days)
