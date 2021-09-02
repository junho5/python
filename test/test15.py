def mask_security_number(security_number):
    result = []
    string = ''
    for i in range(len(security_number)):
        result.append(security_number[i])
    
    for i in range(-1,-5,-1):
        result[i] = '*'
    
    for i in range(len(result)):
        string += result[i]
    return string
    


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))