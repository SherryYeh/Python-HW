def compute(x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4):   
    if((x1<1000) or (y1<1000) or (z1<1000)):
        print("-1")
    else:
        if((x2>2) or (y2>2) or (z2>2)):
            print("-1")
        else:
            if((x3>59)or(x4>59)or(y3>59)or(y4>59)or(z3>59)or(z4>59)):
                print("-1")
            else:
                if(x3==y3 or x3==y4):
                    print("%d,%d,%d"%(x1,y1,x3))
                if(x4==y3 or x4==y4):
                    print("%d,%d,%d"%(x1,y1,x4))
                if(z3==x3 or z3==x4):
                    print("%d,%d,%d"%(x1,z1,z3))
                if(z4==x3 or z4==x4):
                    print("%d,%d,%d"%(x1,z1,z4))
                if(y3==z3 or y3==z4):
                    print("%d,%d,%d"%(y1,z1,y3))
                if(y4==z3 or y4==z4):
                    print("%d,%d,%d"%(y1,z1,y4))
                else:
                    print("correct")		
def main():
    x1=int(input())
    x2=int(input())
    if(x2==1):
        x3=int(input())
        x4=1
    else:
        x3=int(input())
        x4=int(input())
    y1=int(input())
    y2=int(input())
    y3=int(input())
    y4=int(input())
    z1=int(input())
    z2=int(input())
    z3=int(input())
    z4=int(input())
    compute(x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4)
main()