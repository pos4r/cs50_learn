# > (больше) / => (больше или равно) | < (меньше) / <= (меньше или равно) | == (равно) / != (не равно)  

# if (если)

'''
x = int(input("Please put wtite your number: "))
y = int(input("Please put one more number: "))

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal  y")
'''

# elif (иначе если)

'''
x = int(input("Please put wtite your number: "))
y = int(input("Please put one more number: "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal  y")
'''

# else (иначе)

'''
x = int(input("Please put wtite your number: "))
y = int(input("Please put one more number: "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal  y")
'''

# or (или)
'''
x = int(input("Please put wtite your number: "))
y = int(input("Please put one more number: "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''
'''
x = int(input("Please put wtite your number: "))
y = int(input("Please put one more number: "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''

# and (и)

'''
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")

elif score >= 80 and score <= 89:
    print("Grade: B")

elif score >= 70 and score < 80:
    print("Grade: C")

elif score > 59 and score <70:
    print("Grade: D")

elif score >49 and score < 60:
    print("Grade: E")

else:
    print("You not pass")
'''
'''
score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")

elif 80 <= score <= 89:
    print("Grade: B")

elif 70 <= score < 80:
    print("Grade: C")

elif 60 <= score <70:
    print("Grade: D")

elif 50 <= score < 60:
    print("Grade: E")

else:
    print("You not pass")
'''
'''
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

elif score >= 50:
    print("Grade: E")

else:
    print("You not pass")
'''

'''
x = int(input("Write your nimber: "))

if x % 2 == 0:
    print("Your number is  even")

else:
    print("Your number is not even")
'''
'''
def main():
    x = int(input("Write your number: "))
    if is_even(x):
        print("Event")
    else:
        print("0dd")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
main()
'''

'''
def main():
    x = int(input("Write your number: "))
    if is_even(x):
        print("Event")
    else:
        print("0dd")

def is_even(number):
    return True if number % 2 == 0 else False
main()
'''

'''
def main():
    x = int(input("Write your number: "))
    if is_even(x):
        print("Event")
    else:
        print("0dd")

def is_even(number):
    return number % 2 == 0
main()
'''
'''
name = input("What is your name?: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffinodr")
elif name == "Draco":
    print("Slytherin")
else:
    print("WHo?")
'''
'''
name = input("What is your name?: ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case 'Draco'
        print("Slytherin")
    case _:
        print("Who?")
'''