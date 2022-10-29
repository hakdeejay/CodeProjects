###
# for in loop
###
fav_linux_distros = ['Mint', 'Debian', 'Ubuntu', 'Manjaro', 'Fedora', 'Arch']

print('Here is Agent M\'s list of favourite Linux distributions.\n')

for distro in fav_linux_distros:
    print(distro)
    print('\t' + distro + ' is an excellent Linux distribution.')
    print('\tWouldn\'t you agree that ' + distro + ' is an excellent distro?')

print('\nThose are Agent M\'s top ' + str(len(fav_linux_distros)) + ' Linux distributions.')


print(); print(); print();

###
# for in range loop
###
total_cases = 10
total_solved = 7
total_unsolved = total_cases - total_solved

for x in range(1,total_unsolved+1):
    print('| |')

for x in range(1,total_solved+1):
    print('|X|')

print(); print(); print();

###
#for key, value in dictionary loop
###
user_profile = {
          'name': 'Agent M',
          'fav_distro': 'Mint',
          'fav_drink': 'Tea'
          }

for key, value in user_profile.items():
    print('Key: ' + key)
    print('Value: ' + value + '\n')

###
#for value in dictionary loop
###
fav_distros = {
          'q': 'Mint',
          'j': 'Kali',
          'm': 'Ubuntu',
          's': 'Elementary'
          }

for distro in fav_distros.values():
    print(distro)

print(); print(); print();

###
# for in nested loops
###
# Create our 4 agents as their own dictionaries.
agent_m = {
          'name': 'M',
          'distro': 'Ubuntu',
          'drink': 'Earl Grey Tea'
          }

agent_j = {
          'name': 'J',
          'distro': 'Kali',
          'drink': 'Espresso'
          }

agent_s = {
          'name': 'S',
          'distro': 'Elementary',
          'drink': 'Coffee'
          }

agent_q = {
          'name': 'Q',
          'distro': 'Kali',
          'drink': 'Decaf Coffee'
          }

# Combine our agent dictionaries into a single list of agents.
agents = [agent_m, agent_j, agent_s, agent_q]

# Loop through the list of agents so that we get the dictionary
# belonging to each individual agent
for agent in agents:
    # Get the agent's name and print that to the screen
    print('Agent ' + agent['name'] + ':')

    # Loop through that agent's dictionary items
    for key, value in agent.items():

        # If the key isn't the agent's name, print the key and value
        if key != 'name':
            print('\t' + key.title() + ': ' + value)

    # Add an extra return space after an agent's info
    print('\n')
