#pg 77 collatz sequence practice project #this took me wayy too long because i was covering all the posibilities
#made this code myself 
#evaluates numbers to 1 

print('Please enter an integer. ')
#all neg integers and 0 will be converted to a positive integer 
numberinput=input()
def collatz(number):
    try:
        number=abs(int(number))
        while True: #not doing 'while number >= 1:' or 'while number != 1:' to account for all number possibilities
           # if number == 0 or number == 1:
           #     print(1) #you can't input 0 or 1 into below because that leads to something that goes on forever
           #     break
                #got rid of the above code because it repeats 1 twice when evaluating a number
            if number == 0:
                print(1)
                break
            elif number == 1:
                break
            elif (number % 2 == 0): #and (number != 0 or 1): # % gives us remainder #even
                number=number//2 #// get us answer when a is divided by b, rounded to the next smallest whole number
            elif number%2==1: #odd
                number=3*number+1
            print(number)
            
    except:
        print("Hey! You didn't put in an integer!")
collatz(numberinput)