# 현명하게 거스름돈을 계산해 주는 프로그램을 만들려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면,
# 50,000원 1장
# 10,000원 1장
# 5,000원 1장
# 1,000원 2장
# 이런 식으로 '가장 적은 수'의 지폐를 거슬러 주는 것입니다. 방금 같은 경우에는 총 5장을 거슬러 준 거죠.
# 우리는 calculate_change라는 함수를 작성하려고 하는데요. 이 함수는 지불한 금액을 나타내는 payment와 물건의 가격을 나타내는 cost를 파라미터로 받습니다.
# 아래의 코드에 이어서 깔끔하게 프로그램을 작성해 보세요.

def calculate_change(payment, cost):
    charge = payment - cost
    
    fifty = (charge-(charge%50000))/50000
    charge -= fifty*50000
    print("50000원 지폐: {:.0f}장".format(fifty))
    
    onemill = (charge-(charge%10000))/10000
    charge -= onemill*10000
    print("10000원 지폐: {:.0f}장".format(onemill))
    
    five = (charge-(charge%5000))/5000
    charge -= five*5000
    print("5000원 지폐: {:.0f}장".format(five))
    
    thousand = (charge-(charge%1000))/1000
    charge -= thousand*1000
    print("1000원 지폐: {:.0f}장".format(thousand))

# 파이썬의 버림 나눗셈 // 요자식을 이용해서 해봄
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))



# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)