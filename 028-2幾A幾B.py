def ANS():
    ans=[]
    number=[0,1,2,3,4,5,6,7,8,9]
    for i in number:
        for j in number:
            for z in number:
                for k in number:
                    if i!=j and i!=z and i!=k and j!=z and j!=k and z!=k:
                        list=[i,j,z,k]
                        ans.append(list)
    return ans
def main(number,ab,ans):
    numberlist=[]
    re=[]
    count=0
    number=int(number)
    for i in range(4):
        numberlist.append(number%10)
        number//=10
    numberlist=list(reversed(numberlist))
    for i in range(len(ans)):
        if '0A0B' in ab:
            if numberlist[0] in ans[i] or numberlist[1] in ans[i] or numberlist[2] in ans[i] or numberlist[3] in ans[i]:
                re.append(i)
        elif '0A1B' in ab:
            if numberlist[0] == ans[i][0] or numberlist[1] == ans[i][1] or numberlist[2] == ans[i][2] or numberlist[3] == ans[i][3] or len(set(numberlist).intersection(set(ans[i])))!=1 or number==ans[i]:
                re.append(i)
        elif '0A2B' in ab:
            if numberlist[0] == ans[i][0] or numberlist[1] == ans[i][1] or numberlist[2] == ans[i][2] or numberlist[3] == ans[i][3] or len(set(numberlist).intersection(set(ans[i])))!=2 or number==ans[i]:
                re.append(i)
        elif '0A3B' in ab:
            if numberlist[0] == ans[i][0] or numberlist[1] == ans[i][1] or numberlist[2] == ans[i][2] or numberlist[3] == ans[i][3] or len(set(numberlist).intersection(set(ans[i])))!=3 or number==ans[i]:
                re.append(i)
        elif '0A4B' in ab:
            if numberlist[0] == ans[i][0] or numberlist[1] == ans[i][1] or numberlist[2] == ans[i][2] or numberlist[3] == ans[i][3] or len(set(numberlist).intersection(set(ans[i])))!=4 or number==ans[i]:
                re.append(i)
        elif '1A0B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==1 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==1)) or number==ans[i]:
                re.append(i)
        elif '1A1B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==2 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==1)) or number==ans[i]:
                re.append(i)
        elif '1A2B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==3 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==1)) or number==ans[i]:
                re.append(i)
        elif '1A3B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==4 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==1)) or number==ans[i]:
                re.append(i)
        elif '2A0B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==2 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==2)) or number==ans[i]:
                re.append(i)
        elif '2A1B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==3 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==2)) or number==ans[i]:
                re.append(i)
        elif '2A2B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==4 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==2)) or number==ans[i]:
                re.append(i)
        elif '3A0B' in ab:
            if not(len(set(numberlist).intersection(set(ans[i])))==3 and (int(numberlist[0] == ans[i][0]) + int(numberlist[1] == ans[i][1]) + int(numberlist[2] == ans[i][2]) + int(numberlist[3] == ans[i][3])==3)) or number==ans[i]:
                re.append(i)
        elif '4A0B' in ab:
            return numberlist,1
    for i in re:
        ans.remove(ans[i-count])
        count+=1
    if ab =='1':
        print(ans)
    return ans,0
ans=ANS()
while True:
    number,ab=input().split(',')
    ans,x=main(number,ab,ans)
    if len(ans)==1:
        for i in range(4):
            print(ans[0][i],end='')
        print()
        break
    elif x==1:
        for i in range(4):
            print(ans[i],end='')
        print()
        break