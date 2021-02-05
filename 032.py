def compute(t,list1,a,b):
    for i in range(len(t)):
        if(t[i]=="1"):
            list1=right(t,list1,a,b)
        elif(t[i]=="2"):
            list1=right(t,list1,a,b)   
            list1=right(t,list1,a,b)
            list1=right(t,list1,a,b)
        elif(t[i]=="3"):
            list1=right(t,list1,a,b)
            list1=right(t,list1,a,b)
        else:
            print("E")
            return
    for j in range(len(list1)): 
        print("".join(list1[j]))
def right(t,list1,a,b):
    list2=[]
    for j in range(len(list1[0])):
        list3=[]
        for k in range(len(list1)-1,-1,-1):
            list3.append(list1[k][j])
        list2.append(list3)
    return list2
def main():
    list1=[]
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    if(1<=a<=10 and 1<=b<=10):
        for i in range(a):
            n=input()   			
            list1.append(n) 
        t=input() 
        if(len(n)!=b):
            print("E")
            return      
        compute(t,list1,a,b)
    else:
        print("E")
main()