a=str(input("enter the the sentenace"))
b=("aeiou")
count=0
d=[]
for i in (a):
    for j in (b):
        if(i==j):
            d.append(i)
            count=count+1

print(count)
print(d)





