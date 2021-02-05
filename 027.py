def main():
    list=[]
    a,b=map(int,input().split())
    if(a>=10):
        for i in range(a,b+1):
            if(str(i)==str(i)[::-1]):
                list.append(i)
        if(len(list)==0):
            print("0")
        else:
            for i in range(len(list)):
                print(list[i],end=" ")
    else:
        print("0")
main()