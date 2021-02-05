def samesuit(cardsuit):
    same=[cardsuit.count(i)for i in cardsuit]
    if same.count(same[0])==5:
        return True
    else:
        return False
def straight(num):
    same=[num.count(i)for i in num]
    if sum(same)!=5:
        return False
    if(sum(num)-5*min(num))==10:
        return True
    data=[(i+13)if(i<6)else i for i in num]
    if(sum(data)-5*min(data))==10:
        return True
    return False
def pair(num):
    same=[num.count(i) for i in num]
    if same.count(4)==4 or same.count(5)==5:
        return 5
    elif same.count(3)==3 and same.count(2)==2:
        return 4
    elif same.count(3)==3:
        return 3
    elif same.count(2)==4:
        return 2
    elif same.count(2)==2:
        return 1
    else:
        return 0
def test(cards):
    cardsuit=sorted([card[-1] for card in cards])
    cardnum=sorted(map(int,[card[:-1] for card in (cards)]))
    if straight(cardnum)==True and samesuit(cardsuit)==True:
        print('Straight flush')
    elif straight(cardnum)==True:
        print('straight')
    elif pair(cardnum)==5:
        print('four of a kind')
    elif pair(cardnum)==4:
        print('full house')
    elif pair(cardnum)==3:
        print('three of a kind')
    elif pair(cardnum)==2:
        print('two pairs')
    elif pair(cardnum)==1:
        print('one pairs')
def main():
    cards=input().split()
    test(cards)
main()