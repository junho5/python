def is_palindrome(word):
    result = None
    for i in range(len(word)//2):
        check = len(word)-1-i
        if word[i] != word[check]:
            return False
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))