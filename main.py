#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
a = float(input("What was the total bill?\n$"))
b = int(input("How much tip would you like to give?\n% : "))
c = int(input("How many people to split the bill?\nPeople : "))

# Step 1 (tip)
d = (b/100 * a)
e = str(round(d + a))
tip = print("Your Total Cost With Tip Included is " + e + "$")

# Step 2 (Split)
f = int(e)
bill = str(f / c)
print("--------------------------------------------")
print("Each person should pay: $" + bill)
print("--------------------------------------------")
