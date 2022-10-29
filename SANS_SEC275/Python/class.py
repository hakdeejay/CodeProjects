from sympy import Id


class Agent():
        name = ''
        hotDrink = ''

        def __init__(self, id, drink):
                self.name = 'Agent ' + id
                self.hotDrink = drink

        def speak(self, speech):
                print(self.name + ' says: "' + speech + '"')

        def drink(self):
                print(self.name + ' drinks a cup of ' + self.hotDrink)

agentQ = Agent('Q', 'Decaf Coffee')

agentM = Agent('M', 'Coke')

agentN = Agent('N', "Orange Juice")

print()

agentQ.speak("Hi, I'm an agent in black")

agentM.drink()

agentQ.drink()