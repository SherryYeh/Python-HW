def compute(all):
    i=0
    c=0
    for b in range(9):
        part=[]
        a=i*3
        for j in range(a,a+3):
            for k in range(c,c+3):
                part.append(all[j][k])
        if(judge(part)==True):
            c+=3
            if(k==8):
                i+=1
                c=0        
        else:
            print("No")
            return
    print("Yes")
def judge(one):
    for i in range(8):
        for j in range(i+1,9):
            if(one[i]==one[j]):
                return False
    return True
def main():
    list1=[]
    all=[]
    for i in range(9):
        list1=input().split()
        all.append(list1)
    for j in range(9):
        if judge(all[j])==False:
            print("No")
            return
    for k in range(9):
        down=[]
        for h in range(9):
            down.append(all[h][k])
        if judge(down)==False:
            print("No")
            return
    compute(all)
main()