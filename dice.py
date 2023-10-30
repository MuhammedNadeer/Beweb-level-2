import random
import sys

print("Dice Roller 0.1")
print("If you want to roll dice input 'y' else 'n'")
while(1):
    a = input()    
    if a == 'y':
        print("Rolling...")
        print(random.randint(1,6))
    else:
        sys.exit(0)