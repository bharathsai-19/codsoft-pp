def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "can't divisible by zero"
    else:
        return a/b

print("select option:")
print("1.add")
print("2.subtract")
print("1.multiply")
print("1.division")


while True:
    choice = input(" enter the choice(1/2/3/4):")


    if choice in ('1','2','3','4'):
        num1 =float(input("enter the first number"))
        num2 =float(input("enter the second number"))

        if choice=='1':
            print("result",add(num1,num2))
        elif choice=='2':
            print("result",subtract(num1,num2))
        elif choice=='3':
            print("result",multiply(num1,num2))
        elif choice=='4':
            print("result",division(num1,num2))    
        break
    else:
        print("invalid input")