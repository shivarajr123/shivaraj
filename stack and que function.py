from stack_in_class1 import stack1
from Que_opration import Que1

def main():
    b=int(input("select your choice"))
    if b==1:
        stack_name="Stack"
        s1=stack1()
    else:
        stack_name="Que"
        s1=Que1()
    while(True):
        print("options for",stack_name)
        print("1.PUSH")
        print("2.POP")
        print("3.Display")
        print("4.EXIT")
        options=eval(input("enter your choice"))
        if(options==1):
            s1.PUSH()
        elif(options==2):
            s1.POP()
        elif(options==3):
            s1.Display()
        elif(options==4):
            return
        else:
            print("wrong choice")

main()