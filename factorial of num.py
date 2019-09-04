var=eval(input("enter the number:"))
fact=1
if(isinstance(var,int)):
    for i in range(1,var+1):
         fact=fact*i
print("the factorial of",var,\"is",fact)