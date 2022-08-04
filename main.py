import random
# r = "rock"
# p = "paper"
# s = "scissors"
cpu_score = 0
user_score = 0
choices = ["r", "p", "s"]
comp = random.choice(choices)
user = False
#print(user)
# if user == comp:
#     print("TIE!")
# elif user=r and comp=s:
#     print("user wins!!")
# else user=r and comp=p:
#     print("computer wins")
while True:
    user = input(choices)
    if user == comp:
        print("TIE!")
    elif user == "r":
        if comp == "p":
            print("you lose", comp, "covers", user)
            cpu_score += 1
        else:
            print("you win", user, "smashes", comp)
            user_score += 1
    elif user == "p":
        if comp == "s":
            print("you lose", comp, "cuts", user)
            cpu_score += 1
        else:
            print("you win", user, "covers", comp)
            user_score += 1
    elif user == "s":
        if comp == "r":
            print("you lose", comp, "smashes", user)
            cpu_score += 1
        else:
            print("you win", user, "cuts", comp)
            user_score += 1
    elif user == "end":
        print("final score:")
        print("cpu score:" + str(cpu_score))
        print("user score:" + str(user_score))
    else:
        print("invalid choice")
        break





