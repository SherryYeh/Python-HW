import math
def compute(a,b,c,d,e):
    A=(a+b+c+d+e)/5
    X=(a-A)**2+(b-A)**2+(c-A)**2+(d-A)**2+(e-A)**2
    X/=5.0
    Y=math.sqrt(X)
    print("%.2f\n%.2f\n%.2f"%(X,Y,A))
def main():
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    d=int(x[3])
    e=int(x[4])
    compute(a,b,c,d,e)
main()