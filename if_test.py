def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    score = None
    if total >= 90:
        score = 'A'
    elif total >= 80:
        score = 'B'
    elif total >= 70:
        score = 'C'
    elif total >=60:
        score = 'D'
    else:
        score = 'F'
    print(score)
        


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)