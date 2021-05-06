# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
lower = names.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

true = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e

total_score = int(str(love) + str(true))

if total_score >= 40 and total_score <= 50:
    print(f"your score is {total_score}, you are alright together.")
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {total_score}.")
