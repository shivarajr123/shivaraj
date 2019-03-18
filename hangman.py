def fn1(a,d,f,name2):
    n = "".join(a)
    while(n==d):
        print('congratulation you won!!!! ')
        break
    else:
        f -= 1
        if (f!=0):
            fn(f,a,d,name2)
        else:
            print('sorry!!! ' +name2+ ' better luck next time')

def fn(f,a,d,name2):
    g = list(d)
    while (f != 0):
        p = str(input('enter the letter:'))
        l = len(g)
        n="".join(a)
        for i in range(0, l):
            if g[i] == p:
                a[i] = g[i]
                n = "".join(a)
        else:
            print(n)
        fn1(a, d, f,name2)
        break

def main():
    name1 = str(input("what is your name:"))
    print("hello! " + name1 + " shall we start the game")
    d = str(input("enter the guessing word:"))
    print('please give to apposite person')
    f = int(input("how many chances you need to proceed(1 to 15):"))
    name2 = str(input("enter the name"))
    a = []
    for i in d:
        a.append('*')
    fn(f,a,d,name2)
main()
