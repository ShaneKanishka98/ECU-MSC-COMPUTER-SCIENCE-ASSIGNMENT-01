import math
import random
choice = ''

def ask_questions(questions,quantity,minimum,maximum):
    ques_count = 1
    score = 0

    while ques_count <= questions:
        print('Question',ques_count,'of',questions,'.')
        if ques_count < questions:
            score = score + int(random_list(quantity,minimum,maximum))
            print()

        elif ques_count == questions:
            print('Challenge question!')
            score = score + int(random_list(quantity,minimum*2 ,maximum*2))

        ques_count = ques_count + 1

    return int(score)

def random_list(quantity,minimum,maximum):
    quan_count = 1
    array_list = []

    while quan_count <= quantity:
        rand_num = random.randint(minimum, maximum)
        array_list.append(rand_num)
        quan_count = quan_count + 1

    ques_num = random.randint(0, 3)

    return question_array(array_list,ques_num)

def question_array(array_list,ques_num):
    
    que_array = ['What is the smallest number in this list?',
                 'What is the biggest number in this list?',
                 'What is the average of numbers in this list?',
                 'What is the total of numbers in this list?']
    
    print(que_array[ques_num],array_list)

    if(ques_num == 2):
        print('(round UP to nearest integer)')

    user_response = int(input('> '))

    min_value = min(array_list)
    max_value = max(array_list)
    sum_value = sum(array_list)
    avg_value = math.ceil(sum(array_list) / len(array_list))

    if (ques_num == 0):
        if(min_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',min_value,'.')
            return 0
        
    elif (ques_num == 1):
        if(max_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',max_value,'.')
            return 0
        
    elif (ques_num == 2):
        if(avg_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',avg_value,'.')
            return 0

    elif (ques_num == 3):
        if(sum_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',sum_value,'.')
            return 0
    else:
        print('System error! Please contact administrator!!')

while choice != 'E' or choice != 'M' or choice != 'H':
    print('Welcome to the Number List Test program.')
    print('Select a difficulty:\n[E]asy\n[M]edium\n[H]ard')

    choice = input('> ').upper()
    
    if(choice == 'E'):
        print('Easy difficulty selected!\n')
        score = ask_questions(2,3,1,5)
        print('\nTest complete!')
        print('You scored',score,'/',2,'(',score/2*100,'%).')

    elif(choice == 'M'):
        print('Medium difficulty selected!\n')
        score = ask_questions(4,5,3,12)
        print('\nTest complete!')
        print('You scored',score,'/',4,'(',score/4*100,'%).')

    elif(choice == 'H'):
        print('Hard difficulty selected!\n')
        score = ask_questions(6,8,10,25)
        print('\nTest complete!')
        print('You scored',score,'/',6,'(',score/6*100,'%).')

    else:
        print('Invalid choice! Enter E, M or H.')
    
