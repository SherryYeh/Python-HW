def compute(x1,y1,x2,y2):
    m1=(y1-y2)
    m2=(x1-x2)
    b1=(x2*y1-x1*y2)
    b2=(x2-x1)
    if (m1<0 and m2<0):
        m1=-m1
        m2=-m2
    if(b1<0 and b2<0):
        b1=-b1
        b2=-b2
    if(m2<0 and m1>0):
        m2=-m2
        m1=-m1
    if(b2<0 and b1>0):
        b2=-b2
        b1=-b1		
    elif m1==0:
        print("y=%d"%(y1))
        print("y=%d"%(y1))	
    elif m2==0 or b2==0:
        print("x=%d"%x1)
        print("x=%d"%x1)		
    if m2==1:
        if b1==0:
			if(m1==1):
                print("y=x") 
			else:
                print("y=%dx"%m1)
        elif b1%b2==0:
            if(abs(m1)==1):
                if(m1<0):
                    print("y=-x%+d"%(b1/b2))
                    print("y=-x%+d"%(b1/b2))
                else:
                    print("y=x%+d"%(b1/b2))
                    print("y=x%+d"%(b1/b2))
            else:
                print("y=%dx%+d"%(m1,b1/b2))
                print("y=%dx%+d"%(m1,b1/b2))
        elif abs(b2)==1:
            if(abs(m1)==1):
                print("y=x%+d"%b1)
                print("y=x%+d"%b1)
            else:				
                print("y=%dx%+d"%(m1,b1))
                print("y=%dx%+d"%(m1,b1))			
        else:
            if(abs(m1)==1):
                print("y=%x%+.2f"%(b1/b2))
                print("y=%x%+d/%d"%(b1,b2))				
            else:
                print("y=%dx%+.2f"%(m1,b1/b2))
                print("y=%dx%+d/%d"%(m1,b1,b2))				
    elif m1!=0 and m2!=0:
        if b1==0:
            if(m1%m2==0):
                if(abs(m1//m2)==1):
                    if(m1<0 and m2<0 or m1>0 and m2>0):
                        print("y=x")
                        print("y=x")
                    else:
                        print("y=-x")
                        print("y=-x")
                else:
                    print("y=%dx"%(m1/m2))
                    print("y=%dx"%(m1/m2))
            else:
                print("y=%.2fx"%(m1/m2))
                print("y=%d/%dx"%(m1,m2))   
        elif b1%b2==0:
            if(m1%m2==0):
                if(abs(m1//m2)==1):
                    if(m1<0 and m2<0 or m1>0 and m2>0): 
                        print("y=x%+d"%(b1/b2))
                        print("y=x%+d"%(b1/b2))
                    else:
                        print("y=-x%+d"%(b1/b2))
                        print("y=-x%+d"%(b1/b2))					
                else:                  
                    print("y=%dx%+d"%(m1/m2,b1/b2))
                    print("y=%dx%+d"%(m1/m2,b1/b2))											
            else:
                print("y=%.2fx%+d"%(m1/m2,b1/b2))
                print("y=%d/%dx%+d"%(m1,m2,b1/b2))									
        else:
            if(m1%m2==0):
                if(abs(m1//m2)==1):
                    if(m1<0 and m2<0 or m1>0 and m2>0):
                        print("y=x%+.2f"%(b1/b2))
                        print("y=x%+d/%d"%(b1,b2))						
                    else:
                        print("y=-x%+.2f"%(b1/b2))  
                        print("y=-x%+d/%d"%(b1,b2))
                else:
                    print("y=%dx%+.2f"%(m1/m2,b1/b2)) 
                    print("y=%d/%dx%+d/%d"%(m1,m2,b1,b2))                
            else:
                print("y=%.2fx%+.2f"%(m1/m2,b1/b2)) 
                print("y=%d/%dx%+d/%d"%(m1,m2,b1,b2))           
def main():
    t=input().split()
    for i in t:
        if("." in i):
            print("Error!")
            return    
    x1=int(t[0])
    y1=int(t[1])
    x2=int(t[2])
    y2=int(t[3])
    compute(x1,y1,x2,y2)
main()