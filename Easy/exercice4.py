list=[]

def generate_List():
    while True:
        n = input("Enter a number (or press Enter to stop): ")
        if n == "":
            break
        try:
            n=int(n)
            list.append(n)
        except ValueError:
            print("Please enter a valid integer.")
def orderList():
    list.sort()
    return list

def checkNumberInsideList(num):
    if num in list:
        return f"{num} is inside the list."
    else:
        return f"{num} is not inside the list."

print("Enter a numbers to append to the list  (or press Enter to stop): ")
generate_List()

num = int(input("Enter a number to check if it's in the list: "))
print(orderList())
print(checkNumberInsideList(num))