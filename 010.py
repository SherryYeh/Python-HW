def compare(s1,s2,s3):
    if(s1<183):
        t=183
        cost=183
    elif(183<=s1<383):
        t=s1
        cost=183
    elif(383<=s2<983):
        t=s2
        cost=383
    elif(983<=s3):
        t=s3
        cost=983
    print("%d"%t)
    print("%d"%cost)
def price(x1,x2,x3,x4,x5):
    y1=0.08*x1
    y2=0.139*x2
    y3=0.135*x3
    y4=1.128*x4
    y5=1.483*x5
    s1=y1+y2+y3+y4+y5
    z1=0.07*x1
    z2=0.130*x2
    z3=0.121*x3
    z4=1.128*x4
    z5=1.483*x5
    s2=z1+z2+z3+z4+z5
    w1=0.06*x1
    w2=0.108*x2
    w3=0.101*x3
    w4=1.128*x4
    w5=1.483*x5
    s3=w1+w2+w3+w4+w5
    return s1,s2,s3
def main():
    x1=int(input())
    x2=int(input())
    x3=int(input())
    x4=int(input())
    x5=int(input())
    s1,s2,s3 = price(x1, x2, x3, x4, x5)
    compare(s1, s2, s3)
main()



