import random


question = input("Ask magic 8 ball a question ")
answer = random.randint(1, 8)
    
if answer == 1:
    print("It is certain")

elif answer == 2:
    print("It is decidedly so")

elif answer == 3:

    print("Without a doubt")

elif answer == 4:

    print("Yes definitely")


elif answer == 5:

    print("You may rely on it")


elif answer == 6:

    print("As I see it, yes")


elif answer == 7:

    print("Most likely")


elif answer == 8:

    print("Outlook good")


else:  

    print("That's not a question")

print("The end")