st=str(input("enter the string:"))
l=st.split()
a=len(l)
b_w="is"
s=[]
for i in range(0,a):
    if(l[i]!=b_w):
        s.append(l[i])
    else:
        break
s1=" ".join(s)

print(s1)