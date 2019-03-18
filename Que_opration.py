class Que1():
    def __init__(self):
        self.l1=[]
        self.maxelements = eval(input("enter the max element:"))

    def print_attributes(self):
        print(self.l1)
        print(self.maxelements)



    def PUSH(self):
        if (len(self.l1) < self.maxelements):
            a=eval(input("enter the value:"))
            self.l1.append(a)
        return self.l1

    def POP(self):
        if(len(self.l1)>0):
            self.l1.pop(0)
        else:
            print("stack is empty!!")

    def Display(self):
        print(self.l1)

# def main():
#     s1=Que1()
#     while(True):
#         stack_name="Que"
#         print("options for",stack_name)
#         print("1.PUSH")
#         print("2.POP")
#         print("3.Display")
#         print("4.EXIT")
#         options=eval(input("enter your choice"))
#         if(options==1):
#             s1.PUSH()
#         elif(options==2):
#             s1.POP()
#         elif(options==3):
#             s1.Display()
#         elif(options==4):
#             return
#         else:
#             print("wrong choice")
#
# main()

