import math
def compute(total):
    sum=0
    if(total>=120):
        sum+=120
        total-=120
        if(total>=120):
            sum+=160
            total-=120
            return sum+math.ceil(total/30)*60
        else:
            return sum+math.ceil(total/30)*40			
    else:
        return sum+(total//30)*30          
def time(h1, m1, h2, m2):
    x=h2*60+m2-(h1*60+m1)
    return x    
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
        if(t1<0 or t1>24 or t2>59 or t2<00):
            print("error")	
        if(t3<0 or t3>24 or t4>59 or t4<00):
            print("error")
        if(t5<0 or t5>24 or t6>59 or t6<00):
            print("error")
        if(t7<0 or t7>24 or t8>59 or t8<00):
            print("error")
        if(t9<0 or t9>24 or t10>59 or t10<00):
            print("error")
        if(t11<0 or t11>24 or t12>59 or t12<00):
            print("error")
    else:        
        d1 = time(int(t1), int(t2), int(t3), int(t4))
        d2 = time(int(t5), int(t6), int(t7), int(t8))
        d3 = time(int(t9), int(t10), int(t11), int(t12))
        print(compute(d1))
        print(compute(d2))
        print(compute(d3))
main()