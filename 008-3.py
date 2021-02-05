import math   
def compute(a,b,c):
    d=float(b*b-4*a*c)
    #T=float(math.sqrt(b*b-4*a*c))
    x1=float((-b)/(2*a))
    x2=float((math.sqrt(-d))/(2*a))
    x3=float(((-b)+math.sqrt(d))/(2*a))
    x4=float(((-b)-math.sqrt(d))/(2*a))
    #x3=float((-b+T)/(2*a))
    #x4=float((-b-T)/(2*a))
    if(d>=0):
        
        print("%.1f" %x3)
        print("%.1f" %x4)
    else: 
        
        if(x1==0):
            print("%.1f+%.1fi" %(-x1, x2)) 
            print("%.1f-%.1fi" %(-x1, x2))
        else:
            print("%.1f+%.1fi" %(x1, x2)) 
            print("%.1f-%.1fi" %(x1, x2))
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    compute(a,b,c)
main()