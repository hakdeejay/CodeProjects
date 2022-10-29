first_number = ''
second_number = ''

# get input from user and check for quit signal only
def getInput():
       
       number = input("Please enter a number: ")
       if number =='q':
              print('Bye')
              exit()
       return number

# check number is numeric, report if not
def fetchNumber():

       numIsBad = True

       while(numIsBad):
              numb = getInput()
              try:
                     numb = int(numb)
                     numIsBad = False
              except ValueError:
                     print("Please enter a numeric value")
              continue
       return numb

#main loop of program
print('Please give me 2 numbers and I will divide them.')
print('Enter "q" eto quit.\n')

while True:   
       
       first_number = fetchNumber()
       
       second_number = fetchNumber()
       
       try:
              answer = first_number / second_number
       except ZeroDivisionError:
              print('You can\'t divide by zero! Let\'s start again.')
              continue
       else:
              print('Your answer is: ' + str(answer))
              print('Give me another!\n')