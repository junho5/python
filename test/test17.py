import random

result = random.randint(1,20)
chance = 4
for i in range(chance):
    print(result)
    user_input = int(input("기회가 {}번 남았습니다 :".format(chance-i)))
    if user_input == result:
        print("축하합니다 {}번만에 맞히셨어요".format(i+1))
        break
    elif i==3:
        print("아쉽습니다 정답은 {}였습니다".format(result))
    elif user_input>result:
        print("down")
    elif user_input<result:
        print('up')
    