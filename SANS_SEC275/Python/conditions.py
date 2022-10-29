# Write your program here
from pickle import TRUE


coffeeAvailable = True

print("Agent J arrives at HQ")

if coffeeAvailable:
  print("Agent J will have coffee.")
  
print("In the Afternoon, Agent J goes to the HQ cafe.")

coffeeAvailable = False

if not coffeeAvailable:
        print("Agent J is pissed they're out of coffee")

print("Agent J goes home")