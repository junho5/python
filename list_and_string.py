alphabet_list = ['A','B','C','D','E','F']

print(alphabet_list[0])
print(alphabet_list[3])
print(alphabet_list[-1])
print(alphabet_list[0:5])
print(alphabet_list[:4])
print(alphabet_list[:4])


alphabet_string = "ABCDEF"
print(alphabet_string[0])
print(alphabet_string[3])
print(alphabet_string[-1])
print(alphabet_string[0:5])
print(alphabet_string[:4])
print(alphabet_string[4:])

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = list_1 + list_2
print(list_3)

print(len(list_1))
print(len(alphabet_string))

# list 와 문자열의 다른점 
numbers = [1,2,3,4]
numbers[0] = 5
print(numbers)

numbers_string = "1234"
numbers_string[0] = 5
print(numbers_string)