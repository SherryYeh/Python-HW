def compute(n):
    sum=0
    for i in range(n):
        for j in range(i,n):
            sum+=j
            print(sum)
        if(sum>=n):
            for k in range(i,j):            
                print("j")			
                break
            #elif(sum==n):
                #print(j)
    #if(sum==n):
        #print(j)
def main():
    n=int(input())
    compute(n)
main()