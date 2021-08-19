# 포맷팅

year = 2021
month = 1
day = 26

print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day))

print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성","유재석","빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1,num_2,num_1/num_2))

# 현재 잘 사용하지 않는 포맷팅
name = "오준호"
age = 25
print("나의 이름은 %s 이며 나이는 %d입니다" %(name,age))

# 새로나온 f포맷팅
name = "오준호"
age = 25
print(f"제 이름은 {name} 이며 나이는 {age}입니다")