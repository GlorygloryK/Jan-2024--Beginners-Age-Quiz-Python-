print("Hello, great to have you on our page! Firstly, we'd like to get to know you...What's your name?")
name=input("Enter your name here:")
age= input("Now enter your age:")
age=int(age)

if age>100:
    print("Sorry, you're dead")
elif age>=65:
    print("Enjoy your retirement!")# another random output if the person happens to enter 40 specifically
elif age>40:
    print("You're over the hill") #If the user is over 40, the output is "You're over the hill", as requested
elif age==21:
    print("Congrats on your 21st!") # another response if person enters 21 as their age 
elif age<13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")

print(f"Thank you for your participation {name}!")