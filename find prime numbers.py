var=eval(input("enter the start value:"))
var1=eval(input("enter the last value:"))
for i in range(var,var1+1):
    if (i>1):
        for  j in range (2,i):
            if (i%j==0):
                break
        else:
            print(i)

