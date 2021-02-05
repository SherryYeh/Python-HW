def jud1(y):
    b = []
    for i in range(10):
        for j in range(10):
            if(y[i][j]==0):
                if(y[i][j-2]==1 and y[i][j-1]==1 and y[i][j+1]==1 and y[i][j+2]==1):
                    b.append([i,j])
                if(j!=7 and j!=8 and j!=9):
                    if(y[i][j-1]==1 and y[i][j+1]==1 and y[i][j+2]==1 and y[i][j+3]==1):
                        b.append([i,j])
                if(j!=0 and j!=1 and j!=2):
                    if(y[i][j-3]==1 and y[i][j-2]==1 and y[i][j-1]==1 and y[i][j+1]==1):
                        b.append([i,j])
        for j in range(6):
            if(y[i][j+1]==1 and y[i][j+2]==1 and y[i][j+3]==1 and y[i][j+4]==1):
                b.append([i,j])        
        for j in range(4,10):
            if(y[i][j-1]==1 and y[i][j-2]==1 and y[i][j-3]==1 and y[i][j-4]==1):
                b.append([i,j])
    return b
def jud2(y):
    b = []
    for i in range(10):
        for j in range(10):
            if(y[j][i]==0):
                if(y[j][i-2]==1 and y[j][i-1]==1 and y[j][i+1]==1 and y[j][i+1]==0):
                    b.append([j,i])
                if(i!=7 and i!=8 and i!=9):
                    if(y[j][i-1]==1 and y[j][i+1]==1 and y[j][i+2]==1 and y[j][i+3]==1):
                        b.append([j,i])
                if(i!=0 and i!=1 and i!=2):
                    if(y[j][i-3]==1 and y[j][i-2]==1 and y[j][i-1]==1 and y[j][i+1]==1):
                        b.append([j,i])
    for i in range(10):
        for j in range(6):
            if(y[j+1][i]==1 and y[j+2][i]==1 and y[j+3][i]==1 and y[j+4][i]==1):
                b.append([j,i])
    for i in range(4,10):
        for j in range(10):
                if(y[j-1][i]==1 and y[j-2][i]==1 and y[j-3][i]==1 and y[j-4][i]==1):
                    b.append([j,i])
    return b
def main():
    y = []
    for i in range(10):
        x = list(map(int,input().split()))
        y.append(x)
    listt = []
    list1 = jud1(y)
    list2 = jud2(y)
    list1.extend(list2)
    for i in list1:
        if not i in listt:
            listt.append(i)
    listt = sorted(listt)
    for i in listt:
        print('%d %d'%(i[0],i[1]))
main()