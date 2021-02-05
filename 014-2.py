import math
def compute(d1,d2,d3):
    if((d1<30)or(d2<30)or(d3<30)):
        print("0")
    else:
        if(30<=d1 and d1<=120):
            print((d1//30)*30)
        elif(120<d1 and d1<240):
            print(math.ceil((d1-120)/30)*40+120)
        elif(240<=d1):
            print(math.ceil((d1-240)/30)*60+120+160)
        if(30<=d2<=120):
            print((d2//30)*30)
        elif(120<d2<240):
            print(math.ceil((d2-120)/30)*40+120)
        elif(240<d2):
            print(math.ceil((d2-240)/30)*60+120+160)
        if(30<=d3<=120):
            print((d3//30)*30)
        elif(120<d3<240):
            print(math.ceil((d3-120)/30)*40+120)
        elif(240<d3):
            print(math.ceil((d3-240)/30)*60+120+160)  
def main():
    t1,t2=input().split(":")
    t3,t4=input().split(":")
    t5,t6=input().split(":")
    t7,t8=input().split(":")
    t9,t10=input().split(":")
    t11,t12=input().split(":")
    t1=int(t1)
    t2=int(t2)
    t3=int(t3)
    t4=int(t4)
    t5=int(t5)
    t6=int(t6)
    t7=int(t7)
    t8=int(t8)
    t9=int(t9)
    t10=int(t10)
    t11=int(t11)
    t12=int(t12)
    d1=	t3*60+t4-(t1*60+t2)
    d2=	t7*60+t8-(t5*60+t6)
    d3=	t11*60+t12-(t9*60+t10)
    compute(d1,d2,d3)
main()