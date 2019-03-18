def main():
    try:
        num=eval(input("enter the row value: "))
        for i in range (1,(num+1)):
            for j in range(1,(i+1)):
                print("*",end=" ")
            print()
        if num==0:
            print("please give some input for executing this program ")
    except NameError:
        print("Entered input is not acceptable")
    except SyntaxError:
        print("enter some value")
    except:
         print("something went wrong")
    else:
         print("program is successfully done")
    finally:
         print("program Finished")
main()
