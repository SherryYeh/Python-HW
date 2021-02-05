def compute(list,l):
    sum=0
    list.sort()
    for h in range(l-1):
        if(0<=list[h][0]<=60000 and 0<=list[h][1]<=60000):
            if(list[h][1]>list[h+1][0] and list[h][1]<list[h+1][1]):
                list[h+1][0]=list[h][1]
            elif(list[h][1]>list[h+1][0] and list[h][1]>list[h+1][1]):
                list[h+1][0]=list[h][1]
                list[h+1][1]=list[h][1]
            sum+=list[h][1]-list[h][0]
        else:
            return "E"
    if(list[l-2][1]>list[l-1][0] and list[l-2][1]<list[l-1][1]):
        list[l-1][0]=list[l-2][1]
    elif(list[l-2][1]>list[l-1][0] and list[l-2][1]>list[l-1][1]):
        list[l-1][0]=list[l-2][1]
        list[l-1][1]=list[l-2][1]
    sum+=list[l-1][1]-list[l-1][0]
    return sum
    
def main():
    t=int(input())
    for i in range (t):
        list=[]
        l=int(input())
        if(5000>l>0):
            for j in range (l):
                list.append(input().split())
                for k in range(2):
                    list[j][k]=int(list[j][k])
            sum=compute(list,l)
            print(sum)
        else:
            print("E")
main()