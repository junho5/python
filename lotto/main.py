from random import randint


def generate_numbers(n):
    list = []
    for i in range(n):
        number = randint(1, 45)
        if number not in list:
            list.append(number)
    return list


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


print(draw_winning_numbers())
