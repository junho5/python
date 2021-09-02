# 자리수 합 리턴
def sum_digit(num):
    result = 0
    num = str(num)
    for i in range(len(num)):
        result += int(num[i])
    return result


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit = 1
total = 0
while digit<=1000:
    total += sum_digit(digit)
# 코드를 입력하세요.