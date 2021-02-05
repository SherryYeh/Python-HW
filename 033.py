def compute(all):
    for i in range(10):
        for j in range(10):        
            if(all[i][j]=="0"):
                if(right(i,j,all) or down(i,j,all) or slide1(i,j,all) or slide2(i,j,all)):
                    print(i,j)
def right(i,j,all):
    a=int(j)
    count=0
    while(True):    
        if(a-1<0):
            break
        else:
            a-=1
            if(all[i][a]=="1"):
                count+=1                
            if(all[i][a]=="0"):
                break
    a=int(j)
    while(True):    
        if(a+1>9):
            break
        else:
            a+=1
            if(all[i][a]=="1"):
                  count+=1                
            if(all[i][a]=="0"):
                break                               
    if(count>=4):
        return True
    else:
        return False       
def down(i,j,all):
    a=int(i)
    count=0
    while(True):    
        if(a-1<0):
            break
        else:
            a-=1
            if(all[a][j]=="1"):
                count+=1                
            if(all[a][j]=="0"):
                break
    a=int(i)
    while(True):    
        if(a+1>9):
            break
        else:
            a+=1
            if(all[a][j]=="1"):
                  count+=1                
            if(all[a][j]=="0"):
                break                               
    if(count>=4):
        return True
    else:
        return False        
def slide1(i,j,all):
    a=int(i)
    b=int(j)
    count=0
    while(True):    
        if(a-1<0 or b-1<0):
            break
        else:
            a-=1
            b-=1
            if(all[a][b]=="1"):
                count+=1                
            if(all[a][b]=="0"):
                break
    a=int(i)
    b=int(j)
    while(True):    
        if(a+1>9 or b+1>9):
            break
        else:
            a+=1
            b+=1
            if(all[a][b]=="1"):
                  count+=1                
            if(all[a][b]=="0"):
                break                               
    if(count>=4):
        return True
    else:
        return False
def slide2(i,j,all):
    a=int(i)
    b=int(j)
    count=0
    while(True):    
        if(a+1>9 or b-1<0):
            break
        else:
            a+=1
            b-=1
            if(all[a][b]=="1"):
                count+=1                
            if(all[a][b]=="0"):
                break
    a=int(i)
    b=int(j)
    while(True):    
        if(a-1<0 or b+1>9):
            break
        else:
            a-=1
            b+=1
            if(all[a][b]=="1"):
                  count+=1                
            if(all[a][b]=="0"):
                break                               
    if(count>=4):
        return True
    else:
        return False
def main():
    list1=[]
    all=[]
    for i in range(10):
        list1=input().split()
        all.append(list1)
    compute(all)
main()
