# import calculator  # 같은 폴더에 있을때 하는 방법
import calculator as cal  # 이름 설정
from calculator import add, multiply  # 특정 함수만 가져오기 앞에 함수이름 안써도 가능
from calculator import *  # 다 가져오기


print(cal.add(3, 4))
print(add(3, 4))
