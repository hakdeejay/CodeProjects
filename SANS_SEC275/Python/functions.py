### simple function
### functions must be defined before being called in code

def sayHi():
        print("Welcome Agent")

sayHi()

### function parameters
def agentName(id):
        print("Welcome Agent" + id)

agentName('J')
print()

### multiple parameters
def greet_agent(letter, total_cases, solved_cases):
    print('Hello Agent ' + letter + '!')
    print('\tYou have solved ' + str(solved_cases) + ' cases.')

    percent_solved = solved_cases * 100 / total_cases
    print('\tThat\'s ' + str(percent_solved) + '% of your total cases marked as solved, great job!\n')

greet_agent('J', 11, 8)
greet_agent('M', 15, 12)
greet_agent('Q', 20, 12)
greet_agent('S', 20, 15)

print();

### Single responsibility principle
### good practice to only assign a single use to a function
def greet_agent(letter):
    print('Hello Agent ' + letter + '!')

def solved_case_rate(total_cases, solved_cases):
    percent_solved = solved_cases * 100 / total_cases
    print('\tYou have solved ' + str(solved_cases) + ' cases.')
    print('\tThat\'s ' + str(percent_solved) + '% of your total cases marked as solved, great job!\n')

def agent_status(letter, total_cases, solved_cases):
    greet_agent(letter)
    solved_case_rate(total_cases, solved_cases)

agent_status(letter='J', total_cases=11, solved_cases=8)
agent_status(letter='M', total_cases=15, solved_cases=12)
agent_status(letter='Q', total_cases=20, solved_cases=12)
agent_status(letter='S', total_cases=20, solved_cases=15)

print()

### function returning values
def addition(x, y):
    total = x + y
    return total

calculation = addition(31, 11)
print(calculation)