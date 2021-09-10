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

def count_matching_numbers(list_1, list_2):
    cnt = 0
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i]==list_2[j]:
                cnt += 1
    return cnt        


