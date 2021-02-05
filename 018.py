def compute(n):
    list1=[]
    list2=[]
    t=0
    for i in range (2,n+1):
        if(n%i==0 and f(i)==True):
            s1=1            
            list1.append(i)                                       
            for j in range(1,i+1):    
                s1*=j
            t+=s1
            list2.append(s1)
    for k in range (len(list1)):
        print("%d,%d"%(list1[k],list2[k]))
    print(t)
def f(i):
    for h in range (2,i):
        if(i%h==0):
            return False
    return True
def main():
    n=input()
    if n.isdigit():
        n=int(n)
        if(1000>n>0):
            compute(n)
        else:
            print("E")
    else:
        print("E")
        
main()