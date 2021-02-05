import copy
def compute(many,guess,ans): 
    for j in range(many):
        A=B=0
        fake = copy.deepcopy(ans)
        for k in range(len(ans)):
            if guess[j][k]==fake[0][k]:
                A+=1
                fake[0][k]=10
                guess[j][k]=11
        for k in range(len(ans)):        
            for h in range(len(ans)):       
                if (fake[0][k]==guess[j][h]):
                    B+=1
                    fake[0][k]=10
                    guess[j][h]=11  
    #fake = ans
        print("%dA%dB"%(A,B))
"""def check(list1):   
    for i in range(len(list1)):
        if(9>list1[i] or list1[i]<0):
	        return False
    return True"""
def main():
    i=0
    guess=[]
    many=0
    ans=input().split()
    ans[0]=list(map(int,ans))    
    while(i==0):
        number=input()
        if(number=="-1"):
            break
        else:    
            guess.append(number.split())
            guess[many]=list(map(int,guess[many]))
            many+=1
    compute(many,guess,ans)
main()
