def compute(a1,a2,b1,b2,c1):
    if(b1==10):
        s=a1+a2+b1+b2+c1
    else:
        s=a1+a2+b1+b2
    print(s)
def main():
    a1=int(input())
    a2=int(input())
    b1=int(input())
    b2=int(input())
    if(b1==10):
        c1=int(input())
    else:
        c1=0
    compute(a1,a2,b1,b2,c1)
main()