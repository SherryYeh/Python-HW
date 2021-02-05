def compute(a1,a2,b1,b2,c1,c2):
    if(a2<=b1 and b2>=c1):
	    t=a2-a1+c2-b1
    elif(a2>=b1 and c1>=b2):
        t=b2-a1+c2-c1
    elif(a2>=b1 and b2>=c1):
        t=c2-a1
    else:
        t=a2-a1+b2-b1+c2-c1
    print(t)
def main():
    a1=int(input())
    a2=int(input())
    b1=int(input())
    b2=int(input())
    c1=int(input())
    c2=int(input())
    compute(a1,a2,b1,b2,c1,c2)
main()