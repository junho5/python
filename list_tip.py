# 리스트 안에 해당 값있는지 확인하는 함수 (in) 반대는 (not in)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)


# 중첩 리스트
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]
# 첫 번째 학생의 성적
print(grades[0])
# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])
# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)

# 리버스 거꾸로 뒤집는 함수
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

# 해당 값이 가지고 있는 인덱스 리턴
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

# remove 삭제 함수
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)