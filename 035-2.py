def judge(suit,rank):
    flower = 0
    straight = 0
    pair = 0
    for i in suit:
        if(suit.count(i) == 5):
            flower = 1
            break 
    for i in range(5):
        if(rank[i] == '14'):
            rank[i] = '1'
        rank[i] = int(rank[i])
    if(int(min(rank))<=4 and int(max(rank))==13):
        for i in range(5):        
            if(rank[i]<=4): rank[i]+=13
    rank = sorted(rank)
    minn = int(min(rank))
    for i in range(5):
        rank[i] -= minn
    for i in range(5):
        for j in range(5):
            if(i!=j and rank[i]==rank[j]):
                pair += 1
    if(rank == [0,1,2,3,4]): straight = 1
    if(flower==1 and straight==1): return 7
    elif(straight==1): return 4
    elif(straight==0):
        if(pair == 2): return 1
        elif(pair == 4): return 2
        elif(pair == 6): return 3
        elif(pair == 8): return 5
        elif(pair == 12): return 6
        else: return 0
def main():
    n = input().split()
    suit = [i[-1] for i in n]
    rank = [i[:-1] for i in n]
    print(judge(suit,rank))
main()