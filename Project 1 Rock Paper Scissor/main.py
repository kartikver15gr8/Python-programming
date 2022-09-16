import random       # We imported random module as we need random outputs which we will consider as the output given by computer!!

# Snake Water Gun or Rock Paper Scissors, We can make any game using the same logic as we've used in this
# Below I'm making this famous "Rock, Paper & Scissors" game!

# Below we created a function that takes two argument first is computer and second is us!
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True

print("Comp Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Make Your Choice Rock(r) Paper(p) or Scissor(s)")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
