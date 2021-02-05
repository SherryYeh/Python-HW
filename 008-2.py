import math   
def compute(a,b,c):
    d=float(b*b-4*a*c)
    if(d>=0):
        x3=float(((-b)+math.sqrt(d))/(2*a))
        x4=float(((-b)-math.sqrt(d))/(2*a))
        print("%.2f" %x3)
        print("%.2f" %x4)
    else: 
        x1=float((-b)/(2*a))
        x2=float((math.sqrt(-d))/(2*a))
        if(x1==0):
            print("%.2f+%.2fi" %(-x1, x2)) 
            print("%.2f-%.2fi" %(-x1, x2))
        else:
            print("%.2f+%.2fi" %(x1, x2)) 
            print("%.2f-%.2fi" %(x1, x2))
def main():
    a=float(input())
    b=float(input())
    c=float(input())
    compute(a,b,c)
main()