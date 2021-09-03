# strip 화이트 스페이스 제거

print("     \t      \n      abc     def\n\n\n")
print("     \t      \n      abc     def\n\n\n".strip())


# split
my_string = "1. 2. 3. 4. 5. 6."
print(my_string.split(". "))


print("     \n\n        2       \t      \n      3\t\t\t     4".split()) # 파라미터 아무것도 안넘기면 화이트 스페이스 제거
# split을 해서 list를 만들면 문자열로 됨 주의