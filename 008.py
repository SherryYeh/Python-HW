import math
def output(x11,x12,x21,x22,T):
    if(T>=0):
        x1=x11+x12
        x2=x11-x12
        print("%.1f" %x1)
        print("%.1f" %x2)
    else:	
        print("%.1f+%.1fi" %(x11, x12)) 
        print("%.1f-%.1fi" %(x21, x22))
def compute(a,b,c):
    T=float(math.sqrt(b*b-4*a*c))
    x11=float((-b)/(2*a))
    x12=float((T)/(2*a))
    x21=float((-b)/(2*a))
    x22=float((-T)/(2*a))
    return x11,x12,x21,x22,T
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    x11,x12,x21,x22,T=compute(a,b,c)
    output(x11,x12,x21,x22,T)
main()