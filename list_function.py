numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 갯수

print(numbers)

numbers.append(5)  # 추가 연산 (끝자리에 삽입)
numbers.append(8)
print(numbers)

del numbers[3]  # 3번째 인덱스 값 삭제
print(numbers)

numbers.insert  # 삽입 연산 (원하는 자리 삽입)
numbers.insert(4, 77)
print(numbers)

number = [12, 42, 234, 2, 153, 333, 123, 2]
new_sorted = sorted(number) # 기존의 리스트를 건드리지 않고 새로운 리스트 생성 변수 필요
new_sorted = sorted(number, reverse=True)
print(number)

number.sort() # 기존 리스트를 건드려서 정렬 변수 필요 X
print(number)
