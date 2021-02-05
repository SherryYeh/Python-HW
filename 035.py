def suit(cards):
    a=1
    A=sorted([card[-1] for card in (cards)])
    #print(A)
    for i in range(len(A)-1):
        if(A[i]==A[i+1]):
            a+=1
            #print(a)
    return a
def number(cards):
    j=1
    b=1
    B=sorted(map(int,[card[:-1] for card in (cards)])) 
    #print(B)
    for i in range(len(B)-1):       
        if(B[i]!=B[i+1]):
            b+=1
            if(j==4):
                return 6  				
        else:
            j+=1
    if(B[0]!=B[1]==B[2]==B[3]==B[4]):
        return 6 
    if((B[0]==B[1] and B[2]==B[3]!=B[4]) or B[0]==B[1]!=B[2]and B[3]==B[4] or B[0]!=B[1] and B[1]==B[2] and B[3]==B[4]):
        return "two pair"  
    return b
def cont(cards):
    c=1
    C=sorted(map(int,[card[:-1] for card in (cards)]))
    #print(C)
    if 14 in C and 2 in C:
        c+=1
    for i in range(len(C)-1,0,-1):
        if(C[i]-C[i-1]==1):
            c+=1
    for j in range(c,1,-1):
        if(c==j):
            return j
def compute(cards,A,B,C):
    if(A==5 and C==5):
        print("7")
    elif(B==6):
        print("6")
    elif(B==2):
        print("5")
    elif(C==5):
        print("4")
    elif(B==3):
        print("3")
    elif(B=="two pair"):
        print("2")
    elif(B==4):
        print("1")
    else:
        print("0")   
def main():
    cards=[]
    cards=input().split()
    A=suit(cards)
    B=number(cards)
    C=cont(cards)
    compute(cards,A,B,C)
main()