with open('vocabulary.txt','r')as f:
    for i in f:
        data = i.strip().split(': ')
        answer = input(data[1]+': ')
        if answer == data[0]:
            print('맞았습니다 !\n')
        else:
            print('아쉽습니다. 정답은 {}입니다.'.format(data[0]))