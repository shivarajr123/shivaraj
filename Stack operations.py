def fn(stack):
    l=eval(input("enter the ele:"))
    stack.append(l)
    return stack
def fn1(stack):
    if stack==[]:
        print("stack is empty")
    else:
        stack.pop()
    return stack

def fn2(stack):
    return stack
def fn3():
    exit

def main():
    print("if u need to push the ele in stack press '1' for PUSH, press '2' for POP,press '3' for Display or press '4' for Exit")
    a=eval(input("enter ur choice: "))
    stack=[]
    b=0
    while(True):
        while(b<5):
            if(a==1):
                print(fn(stack))
            elif a==2:
                print(fn1(stack))
            elif a==3:
                print(fn2(stack))
            elif a==4:
                fn3()
            else:
                a=eval(input("enter the correct choice:"))
            a=eval(input("enter the choice:"))
            b = len(stack)
        print("stack is full")
        break
main()