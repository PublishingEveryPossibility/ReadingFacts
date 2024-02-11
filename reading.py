"""
Encouraging users to read more to improve their quality of life through reading stats. 

Setting daily goals will help improve literacy, mental health, self-esteem, lower stress, and improve rest using the program written in Python.

The program will allow the user to input their age and the amount of time they have resourced to enjoy leisure reading. 
The program will return statistics that will show their words per minute average, while displaying statistical integers reflecting a percentage on rest improvement and stress reduction.

All of the information needed to create the formulas to return accurate information will be sited from -

‘http://www.crossrivertherapy.com/research/reading-statistics’ .

"""
user_age = 0 #where user age is stored
time_of_day = '' # answer is stored
user_reading= 0 #user reading time is stored
def user(user_age,time_of_day): # error handling for inputs
    global user_reading
    while True:
        try:
            user_age = int(input('What is your age? '))   #user age input
            if user_age< 18:
                print('Sorry we do not have information for your age group. ') # user age error handling
                pass
            break
        except ValueError:
            print('Invalid input. Please enter an integer for your age.')#error handling continued
    while True:
        try:
            user_reading = int(input('How much time do you read everyday? [minutes] ')) # user input reading time
            break
        except ValueError:
            print('Invalid input. Please enter an integer for your reading time.') #reading time error handling

    while True:
        time_of_day = input('When do you read [morning:noon:night]? ') # user input
        if time_of_day in ['morning', 'noon', 'night']:
            break
        else:
            print('Invalid input. Please enter "morning", "noon", or "night".') #user input error handling
 

    return user_age,time_of_day




def words_read():
    global user_reading 
    avg_wpm = 250 * user_reading #users estimated average words per day
    avg_page = 2 * user_reading # user estimated average pages per day
    
    print('Did you know that you read '+ str( {avg_wpm} ) +  '  words in a day when you read ' + str({user_reading}) + ' minutes per day?')
    print('That is a total of ' + str({avg_page}) + ' pages per day! ')
   
def user_ranking(user_reading):

    if  29 >=int(user_age)< 30: #user age iteration
        i=0
    elif 50 >= int(user_age) >=30:
        i=1
    elif 65 >= int(user_age):
        i=2
    else:
        print('Inclusive information to return user reading statistics.')
    user_percentage = [83,77,72,68] #statistics
    u_per = (100 - user_percentage[i]) # user percentage
    r_group = (f'You are in the '+ str(user_percentage[i])+'\%  of Americans in your age group who read. This directly contributes to America ranking 17th in reading comprehension globally.')
    nn_group = (f'You are in the '+ str(u_per) +'  percentile of Americans in your age group who do not read. This directly contributes to America ranking 17th in reading comprehension globally.')
    
 
    if user_reading > 12: #average reading time information cited from source
        print(r_group)
        if user_reading >=30: #benefits of reading over 30 minutes per day
            print('You are 18% more likely, compared to other Americans, to experience positive self esteem.')
        elif user_reading < 30: #benefits of reading everyday
            print('You are 10% more likely, compared to other Americans, to experience positive self esteem.')
        print('You are also 27% more likely to develop healthy socializing skills while lowering your stress as much as 68%')
    else:
        print(nn_group) #group who does not read
    
    words_read() # processes inputs


    print('Studies show that more than half of the people that read before going to bed have more restful sleep than those who do not.')
    response = str(input('So do you think you could make time to read more? [y or n]'))
    if response == 'y': #if user answers yes
        print('That\'s great!')
    elif response == 'n': # if user answers no
        print('There are so many ways to reimagine the power of reading.')
        print('Just 30 minutes per day can reduce stress, improve sleep, help with self esteem, improve vocabulary and communication skills, as well as influence professional development.')
    
    else: # if anything but 'y' or 'n' is input
        print('I\'m sorry I do not understand. Maybe you should read more...')
        print('Audiobooks count... not sure if that helps.')



user(user_age,time_of_day) #input function is started
user_ranking(user_reading)# user information is processed and returned
