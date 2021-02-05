def compute(k):
    for i in range(k,1,-1):
        if(judge(i)==True):        
            print(i)
            break
def judge(i):     
    for j in range(2,i):
        if(i%j==0): 
            return False
    return True   
def main():
    x=input().split(".")
    x[0]=int(x[0])
    if(len(x)>1):
        x[1]=int(x[1])   
        if(x[0]>0):
            k=x[0]
        elif(x[0]<0):
            k=x[1]
        compute(k)
    else:           
        if(x[0]==0 or x[0]==1):
            k=1000
        elif(x[0]<0):
            k=x[0]*-11
        elif(1000>=x[0]>=2):
            k=x[0]       
        else:
            print("Error!")
            return
        compute(k)
main()