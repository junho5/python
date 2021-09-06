from random import randint


def generate_numbers(n):
    list = []
    for i in range(n):
        number = randint(1,45)
        list.append(number)
    return list

print(generate_numbers(6))