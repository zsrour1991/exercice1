def isEven(num):
    if int(num) % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

def isDivideBy4(num):
    if int(num) % 4 == 0:
        return "Number is divisible by 4"
    else:
        return "Number is not divisible by 4"

def check(num,num2):
    if int(num) % int(num2) == 0:
        return f"{int(num)} is divisible by {int(num2)}"
    else:
        return f"{int(num)} is not divisible by {int(num2)}"

number=""
number2=""
checked=""
number=input("Enter a number: ")
print(isEven(number)) 
print(isDivideBy4(number))
number2=input("Enter another number: ")
checked=input("Enter another number: ")
print(check(number, checked))
