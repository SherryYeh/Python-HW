def compute(many,x):
    for j in range(many):
        n=int((x[j][1]))
        if 1<=x[j][1]<19 and x[j][0]==1 and 1<=x[j][0]<3 and x[j][1]!=2 and x[j][1]!=4 and x[j][1]!=6 and x[j][1]!=8 and x[j][1]!=10 and x[j][1]!=12 and x[j][1]!=14 and x[j][1]!=16 and x[j][1]!=18: 
            for k in range(n):
                if k<=(n//2):
                    for many in range(k,(n//2)):
                        print('.',end='')
                    for many in range(1,k+2,1):
                        print(many,end='')  
                    for many in range(k,0,-1):
                        print(many,end='')
                    print()    
                else:
                    for many in range((n//2),k):
                        print('.',end='')
                    for many in range(1,n-k+1,1):
                        print(many,end='')  
                    for many in range(n-k-1,0,-1):
                        print(many,end='')
                    print()
        elif (x[j][1]>5 or x[j][1]<1) and x[j][0]==2:
            print('E')                   
        if 1<=x[j][1]<=5 and x[j][0]==2 and 1<=x[j][0]<=2:
            for k in range(n):
                for many in range(n,n+k):
                    print('.',end='')
                for many in range(0,n-k):
                    print(2*(n-k-many)-1,end='')
                for many in range(1,n-k):
                    print(2*many+1,end='')
                print()					
        elif x[j][0]==1 and (x[j][1]>18 or x[j][1]<1):
            print('E')
        elif x[j][0]==1 and (x[j][1]==2 or x[j][1]==4 or x[j][1]==6 or x[j][1]==8 or x[j][1]==10 or x[j][1]==12 or x[j][1]==14 or x[j][1]==16 or x[j][1]==18):
            print('E')        
        elif x[j][0]<=0 or x[j][0]>=3:
            print('E')
        print()
def main():
    i="Y"
    x=[]    
    many=0
    while(i=="Y"):
        a=input()
        if(a=="-1"):
            break
        else:
            x.append(a.split())
            x[many]=list(map(int,x[many]))
            many+=1
    compute(many,x)	
main()