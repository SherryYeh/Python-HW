def compute(a1,a2,a3,a4):
    if(a4-a3==a3-a2==a2-a1):
        a5=a4+a4-a3
    elif(a4/a3==a3/a2==a2/a1):
        a5=a4/a3*a4
    else:
        print("E")
    a5=int(a5)
    print("%d %d %d %d %d"%(a1,a2,a3,a4,a5))
def main():
    t=int(input())
    if(1<=t<=20):        
        for j in range(t):
            a1,a2,a3,a4=input().split()
            a1=int(a1)
            a2=int(a2)
            a3=int(a3)
            a4=int(a4)
            compute(a1,a2,a3,a4)
    else:
        print("E")
main()