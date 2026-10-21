list=[]
tempList=[]

def generateList():
    while True:
       
        n = input("Enter a number (or press Enter to stop): ")
        if n == "":
            break
        try:
            n=int(n)
            list.append(n)
        except ValueError:
            print("Please enter a valid integer.")

def firstNumberAndLastNumber():
    if len(list) > 0:
        first = list[0]
        last = list[-1]
        tempList.append(first)
        tempList.append(last)
    else:
        print("The list is empty.")

generateList()
firstNumberAndLastNumber()
print(list)
print(tempList)