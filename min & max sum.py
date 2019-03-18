def min_sum():
    s = []
    for i in range(4):
        s.append(a[i])
    print(s)
    print(sum(s))

def max_sum():
    s1 = []
    a.reverse()
    for i in range(4):
        s1.append(a[i])
    print(s1)
    print(sum(s1))

def main():
    n1=eval(input("enter the list: of 6 numbers"))
    a=list(n1)
    a.sort()
    print(a)
    min_sume()
    max_sum()
main()






