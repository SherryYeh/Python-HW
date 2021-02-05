def compute(s1,s2):
    if(s1>s2):
        d=0.6
    else:
        d=0
    return d
def calculate(m,d,s1,s2):
    if(9>=m>=7):
        if(s2<=120):
            t1=s2*2.10-(s1-s2)*d
        elif(121<=s2<=330):
            t1=s2*3.02-(s1-s2)*d
        elif(331<=s2<=500):
            t1=s2*4.39-(s1-s2)*d
        elif(501<=s2<=700):
            t1=s2*4.97-(s1-s2)*d
        else:
            t1=s2*5.63-(s1-s2)*d
    else:
        if(s2<=120):
            t1=s2*2.10-(s1-s2)*d
        elif(121<=s2<=330):
            t1=s2*2.68-(s1-s2)*d
        elif(331<=s2<=500):
            t1=s2*3.61-(s1-s2)*d
        elif(501<=s2<=700):
            t1=s2*4.01-(s1-s2)*d
        else:
            t1=s2*4.50-(s1-s2)*d
    t1=float(t1)
    print("%.2f"%t1)			
def main():
    m=int(input())
    s1=int(input())
    s2=int(input())
    d=compute(s1,s2)
    calculate(m,d,s1,s2)
main()