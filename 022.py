def compute(many,x):
    for j in range(many):
        n=x[j][1]
        if x[j][0]==1 and 1<=x[j][1]<=17 and x[j][1]!=2 and x[j][1]!=4 and x[j][1]!=6 and x[j][1]!=8 and x[j][1]!=10 and x[j][1]!=12 and x[j][1]!=14 and x[j][1]!=16:
            for k in range(n):
                if k<=(n//2):
                    for i in range(k,(n//2)):
                        print(".",end="")
                    for i in range(1,k+2):
                        print(i,end="")
                    for i in range(k,0,-1):
                        print(i,end="")
                    print()
                else:
                    for i in range(n//2,k):
                        print(".",end="")
                    for i in range(1,n-k+1):
                        print(i,end="")
                    for i in range(n-k-1,0,-1):
                        print(i,end="")
                    print()
        elif x[j][0]==2 and 1<=x[j][1]<=5:
            for k in range(n):
                for i in range(0,k):  
                    print(".",end="")
                for i in range(2*(n-k)-1,0,-2):
                    print(i,end="")
                for i in range(3,2*(n-k),2):
                    print(i,end="")
                print()					
        else:
            print("E")
        print()			
def main():
    x=[]
    many=0
    while(True):
        a=input()
        if(a=="-1"):
            break
        else:
            x.append(a.split())
            x[many]=list(map(int,x[many]))
            many+=1
    compute(many,x)
main()