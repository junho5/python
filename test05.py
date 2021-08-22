i = 1
current = 1
previous = 0
# while i <= 50:
#     print(current)
#     temp = previous
#     previous = current
#     current = current + temp
#     i += 1
    
while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1