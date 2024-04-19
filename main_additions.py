# random and time library 
import random
import time

# The user difficulty selection variable is set to null initially because it needs to enter the loop during the first iteration.
difficulty = ''

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
            score = score + int(random_list(quantity,minimum*2,maximum*2))
        
        ques_count = ques_count + 1

    return int(score)

def random_list(quantity,minimum,maximum):
    array_list = []
    quan_count = 1
    ques_num = 1

    while quan_count <= quantity:
        rand_num = random.randint(minimum, maximum)
        array_list.append(rand_num)
        quan_count = quan_count + 1
    
    ques_num = random.randint(0, 5)

    return question_array(array_list,ques_num)

def question_array(array_list,ques_num):
    
    min_value = min(array_list)
    max_value = max(array_list)
    sum_value = sum(array_list)
    avg_value = int(round(sum(array_list) / len(array_list),0))
    dif_min_max_value = max(array_list) - min(array_list)
    
    # random number selected from the list
    random_choice = random.choice(array_list)
    # how many times it's existing
    check_exist = int(array_list.count(random_choice))

    que_array = ['What is the smallest number in this list?',
                 'What is the biggest number in this list?',
                 'What is the average of numbers in this list?',
                 'What is the total of numbers in this list?',
                 'What is the difference between the smallest and biggest numbers in this list?',
                 'How many '+str(random_choice)+'s are there in this list?']
    
    print(que_array[ques_num],array_list)
    
    start = time.time()

    while True:
        try:
            user_response = int(input())
            break
        except ValueError:
            print('Invalid Input!')
        
    end = time.time()
    elapsed = end-start

    if (ques_num == 0):
        if(min_value == user_response):
            print('Correct! You answered in',round(float(elapsed),2),'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',min_value,'.')
            return 0
    elif (ques_num == 1):
        if(max_value == user_response):
            print('Correct! You answered in',round(float(elapsed),2),'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',max_value,'.')
            return 0
    elif (ques_num == 2):
        if(avg_value == user_response):
            print('Correct! You answered in',round(float(elapsed),2) ,'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',avg_value,'.')
            return 0
    elif (ques_num == 3):
        if(sum_value == user_response):
            print('Correct! You answered in',round(float(elapsed),2),'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',sum_value,'.')
            return 0
    elif (ques_num == 4):
        if(dif_min_max_value == user_response):
            print('Correct! You answered in',round(float(elapsed),2),'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',dif_min_max_value,'.')
            return 0
    elif (ques_num == 5):
        if(check_exist == user_response):
            print('Correct! You answered in',round(float(elapsed),2),'seconds')
            return 1
        else:
            print('Incorrect! Correct answer was',check_exist,'.')
            return 0
    else:
        print('System error! Please contact administrator!!')

# Header for a program
print('Welcome to the Number List Test program.')

# Looping the program 
while difficulty != 'E' or difficulty != 'EASY' or difficulty != 'M' or difficulty != 'MEDIUM' or difficulty != 'H' or difficulty != 'HARD':
    
    # Program Instruction
    print('Select a difficulty:\n[E]asy\n[M]edium\n[H]ard')

    # User input for difficulty mode
    difficulty = input('> ').upper()
    
    # Difficulty mode is EASY ('E')
    if(difficulty == 'E' or difficulty == 'EASY' ):
        print('Easy difficulty selected!\n')
        score = ask_questions(2,3,1,5)
        print('\nTest complete!')
        print('You scored',score,'/',2,'(',score/2*100,'%).')

    # Difficulty mode is MEDIUM ('M')
    elif(difficulty == 'M' or difficulty == 'MEDIUM'):
        print('Medium difficulty selected!\n')
        score = ask_questions(4,5,3,12)
        print('\nTest complete!')
        print('You scored',score,'/',4,'(',score/4*100,'%).')

    # Difficulty mode is HARD ('H')
    elif(difficulty == 'H' or difficulty == 'HARD'):
        print('Hard difficulty selected!\n')
        score = ask_questions(6,8,10,25)
        print('\nTest complete!')
        print('You scored',score,'/',6,'(',score/6*100,'%).')

    # Invalid Mode
    else:
        print('Invalid choice! Enter E/EASY, M/MEDIUM or H/HARD.')
    
