a=eval(input("enter the first numbers"))
b=eval(input("enter the second number"))
if (a<b):
    for i in range (a,b+1):
        if(i%2==0):
            print("this is even number:", i)
        else:
            print("this is odd number:", i)
else:
    print("please enter the valid input")