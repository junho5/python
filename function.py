def print_square(x):
  print(x*x)

def get_square(x):
  return x*x


print_square(3) # 9출력
get_square(3) # 아무값도 출력 x

print(print_square(3)) # 9출력 후 none출력
print(get_square(3)) # 9출력

# 옵셔널 파라미터 (기본값 함수한테 주기) 줄때 무조건 마지막 중간에 주면 오류 발생
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우
