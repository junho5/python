numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
for i in range(len(numbers)//2):
    right = len(numbers) - i - 1
    numbers[right], numbers[i] = numbers[i], numbers[right]


print("뒤집어진 리스트: " + str(numbers))
