import random
choice = ''

# ▪ Easy difficulty… questions = 2, quantity = 3, minimum = 1, maximum = 5.
# ▪ Medium difficulty… questions = 4, quantity = 5, minimum = 3, maximum = 12.
# ▪ Hard difficulty… questions = 6, quantity = 8, minimum = 10, maximum = 25.
def ask_questions(questions,quantity,minimum,maximum):
    
    # Question count 
    ques_count = 1
    
    # Score count
    score = 0

    # Question looping
    # ▪ Easy difficulty… questions = 2
    # ▪ Medium difficulty… questions = 4
    # ▪ Hard difficulty… questions = 6
    while ques_count <= questions:
        
        # Print Question No.  
        print('Question',ques_count,'of',questions,'.')

        # Check the pre-define question count lower than ques count 
        if ques_count < questions:
            # Calculate Score
            score = score + int(random_list(quantity,minimum,maximum))
            # Space
            print()

            #Challenge Question
        elif ques_count == questions:
            print('Challenge question!')
            # Calculate Score
            score = score + int(random_list(quantity,minimum*2,maximum*2))

        # Increment question count
        ques_count = ques_count + 1

    # return score
    return int(score)

# random_list function
def random_list(quantity,minimum,maximum):

    # temporary array
    array_list = []

    # Quantity count 
    quan_count = 1

    # Create question array
    while quan_count <= quantity:

        # Generate random number
        rand_num = random.randint(minimum, maximum)

        # Append to array
        array_list.append(rand_num)

        # Quantity increment
        quan_count = quan_count + 1
    
    # Generate random question no
    ques_num = random.randint(0, 3)

    # Return the array and question number for the exam :)
    return question_array(array_list,ques_num)

def question_array(array_list,ques_num):
    
    # Question bundle
    que_array = ['What is the smallest number in this list?',
                 'What is the biggest number in this list?',
                 'What is the average of numbers in this list?',
                 'What is the total of numbers in this list?']
    
    # Print Question and array list
    print(que_array[ques_num],array_list)

    # Average Question then print to enter it rounds up to nearest integer
    if(ques_num == 2):
        print('(round UP to nearest integer)')

    # Get answer from the user
    user_response = int(input('> '))

    # Calculate MIN
    min_value = min(array_list)
    
    # Calculate MAX
    max_value = max(array_list)

    # Calculate SUM
    sum_value = sum(array_list)

    # Calculate AVERAGE
    avg_value = int(round(sum(array_list) / len(array_list),0))

    # Question 01 (MIN)
    if (ques_num == 0):
        if(min_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',min_value,'.')
            return 0
        
    # Question 02 (MAX)
    elif (ques_num == 1):
        if(max_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',max_value,'.')
            return 0
    
    # Question 03 (AVERAGE)
    elif (ques_num == 2):
        if(avg_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',avg_value,'.')
            return 0
    
    # Question 04 (SUM)
    elif (ques_num == 3):
        if(sum_value == user_response):
            print('Correct!')
            return 1
        else:
            print('Incorrect! Correct answer was',sum_value,'.')
            return 0
        
    # Invalid Question
    else:
        print('System error! Please contact administrator!!')


# Validate the user's input and continue looping until it matches 'E', 'M', or 'H', regardless of case.
while choice != 'E' or choice != 'M' or choice != 'H':

    # Title of the Number Testing Program
    print('Welcome to the Number List Test program.')

    # Instruction for the Number Testing Program
    print('Select a difficulty:\n[E]asy\n[M]edium\n[H]ard')

    # Request user input for 'choice'.
    choice = input('> ').upper()
    
    # Verify if the choice matches 'E'.
    if(choice == 'E'):

        # Title for EASY mode
        print('Easy difficulty selected!\n')

        # Criteria for EASY mode
        score = ask_questions(2,3,1,5)

        # Completion message
        print('\nTest complete!')

        # Score Calculation
        print('You scored',score,'/',2,'(',score/2*100,'%).')

    # Verify if the choice matches 'M'.
    elif(choice == 'M'):

        # Title for MEDIUM mode
        print('Medium difficulty selected!\n')

        # Criteria for MEDIUM mode
        score = ask_questions(4,5,3,12)

        # Completion message
        print('\nTest complete!')

        # Score Calculation
        print('You scored',score,'/',4,'(',score/4*100,'%).')
    
    # Verify if the choice matches 'H'.
    elif(choice == 'H'):

        # Title for HARD mode
        print('Hard difficulty selected!\n')

        # Criteria for HARD mode
        score = ask_questions(6,8,10,25)

        # Completion message
        print('\nTest complete!')

        # Score Calculation
        print('You scored',score,'/',6,'(',score/6*100,'%).')

    # Invalid choice
    else:
        print('Invalid choice! Enter E, M or H.')
    
