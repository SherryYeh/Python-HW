def ABfunc(n,total):
    A=B=0
    for i in range(4):        
        if(n[i]==total[i]):    
            A+=1
    for i in range(4):
        for j in range(4):
            if(n[i]==total[j]):
                B+=1
    B-=A
    return(str(A)+"A"+str(B)+"B")
def main():
    list=[]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for g in range(10):
                    if(i!=j and i!=k and i!=g and j!=k and j!=g and k!=g):			
                        list.append(str(i)+str(j)+str(k)+str(g))
    while(len(list)!=1): 
        n=input().split(",")
        w=0
        while(len(list)>w):           		
            AB=ABfunc(n[0],list[w])
            if(AB!=n[1]):
                del list[w]
            else:
                w+=1
    print(list[0])
main()