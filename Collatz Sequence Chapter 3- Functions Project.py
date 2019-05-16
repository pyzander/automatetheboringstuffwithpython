#Collatz Sequence Practice Project #evaluates numbers to 1 #pg 77 
#decided to make this because I didn't see anyone else with code that covered the posibilities of negative numbers, 0, 1 and non-numbers


print('Please enter an integer.')
numberinput=input()

def collatz(number):
    try:
        number=abs(int(number)) #all neg integers will be converted to a positive integer 
        while True: #not doing 'while number >= 1:' or 'while number != 1:' to account for all number possibilities
            if number == 0:
                print(1)
                break
            elif number == 1:
                break
            elif number % 2 == 0: #and (number != 0 or 1): # % gives us remainder #even
                number=number//2 #// get us answer when a is divided by b, rounded to the next smallest whole number
            elif number%2==1: #odd
                number=3*number+1
            print(number)          
    except:
        print("Hey! You didn't put in an integer!")

collatz(numberinput)