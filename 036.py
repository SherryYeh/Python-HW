def compute(big,P,Pnum2,z,times): 
    a=0
    b=0
    c=0
    d=0
    x=""
    for i in range(3):
        #print("z1=%d"%z)
        if(z==4):
            z=0
        cards=input().split()
        #print(times)
        if(times==5):
            y=input().split()
            #print(y) 
            w=input().split()		
            print("ERROR")
            return
        suit1=list(card[-1] for card in cards)
        suit2=sorted(suit1)
        num1=list(map(int,(card[:-1] for card in cards)))
        num2=sorted(num1)
        #print(num2)
        #print(suit1)
        for j in range(4):
            if cards[j] in P[z]:
                if(z==3):
                    z=-1					
                z+=1
                #print(z)
            else:
                #print(j)
                if(i==0):
                    y=input().split()
                    w=input().split()
                if(i==1):
                    y=input().split()
                print("ERROR") 
                return				
        for k in range(1,4):
            if (suit2[0]!=suit2[k]):
                z=z+k-1
                if z>=4:
                   z=z%4
                if cards[0][1] in P[z][1]:
                    if(i==0):
                        y=input().split()
                        w=input().split() 
                    if(i==1):
                        y=input().split()
                    print("ERROR")
                    return
        #print("z2=%d"%z)
        z=output(suit2,num1,num2,big,z,P,cards)
        if(z==0):
            a+=1
        if(z==1):
            b+=1   
        if(z==2):
            c+=1	
        if(z==3):
            d+=1	

    if(x=="ERROR"):
        print("ERROR")
        return
    print(a)
    print(b)
    print(c)
    print(d)
    if(a+c>b+d):
        print("P1 P3")
    else:
        print("P2 P4")
def output(suit2,num1,num2,big,z,P,cards):
    print(z)
    if(suit2[0]==suit2[1]==suit2[2]==suit2[3]):   
        for i in range(4):
            if 1==num1[i]:
                z=z+i
                if z>=4:
                    z=z%4
                    if(z==0):
                        z=4
                #print(z)
        for k in range(4):
            if (1==num2[0] and str(num2[0]) in cards[k]):
                #print(k)
                z=z+k
                #print(z)
            elif str(num2[3]) in cards[k]:
                #print(num2[3])
                z=z+k
                print(z)			
        if(z>=4):
            z=z%4	
        #print("z3=%d"%z)
    else:
        #print("output2")    
        for j in range(3):
            if (suit2[j]!=suit2[j+1]):
                for k in range(13): 
                    if suit2[j]==P[z][k][1]:
                       #print(P[z])
                        z=10
                        print("ERROR")
                        break
        if(big in suit2):
            for i in range(4):
                if (1==num1[i]):
                    """z=z+i
                    if z>=4:
                        z=z%4"""
                    O=1
                else:
                    for k in range(4):
                        if num2[j] in P[k]:
                            z=z+k
            if(z>=4):
                z=z%4    
        #print("z4=%d"%z)							
    return z
def main():
    z=0
    big=0
    Psuit1=[]
    Psuit2=[]
    Pnum1=[]
    Pnum2=[]
    P=[]
    for i in range(4):
        n=input().split()
        P.append(n)
    #print(P[0][2][1])
    for i in range(4):
        Psuit1=sorted(card[-1] for card in P[i])
        Psuit2.append(Psuit1)
        Pnum1=sorted(map(int,[card2[:-1] for card2 in P[i]]))
        Pnum2.append(Pnum1)
    #print(Psuit1)
    #print(Pnum2)
    a=0
    times=0
    while(True):
        n=input()    
        if(z==4):
            z=0
        #print("z=%d"%z)  
        if(n!="pass"):
            a=0
            big=n[-1]
            times+=1
            #print("t=%d"%times) 
            if(times==5):
                break
        elif(n=="pass"):
            times==0			
            a+=1
            #print("a=%d"%a)
            if(a==3):
                z+=2
                #print("big=%s"%big)
                break 
        z+=1
    #print(times)  
    if(times==5):
        a=0
        while(True):
            n=input()
            #print("n=%s"%n)
            if(n=="pass"):
                a+=1
            #print(a)
            if(a==3):
                break		
    compute(big,P,Pnum2,z,times)  
main()