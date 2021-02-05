def f1(x):
    return int(x[:-1])*10+(4-(ord(x[-1])-65))
def next(player):
    return 0 if player==3 else player+1
def f2(x):
    num=14 if x.replace(x[-1], "") == '1' else int(x.replace(x[-1], ""))
    sut=5 if 4-(ord(x[-1])-65)==suit else 4-(ord(x[-1])-65)
    return sut*100+num
def call(passCount=0,player=0,point=0,who=0):
    while passCount!=3:
        temp=input()
        if temp=='pass':
            if point==0:
                raise Exception
            passCount+=1
        elif f1(temp)>point and f1(temp)<40 and temp[-1] in 'ABCD':
            passCount,player,point=0,who,f1(temp)
        else:
            raise Exception
        who=next(who)
    return player,point//10,point%10
def pk(cards,player):
    temp=input().split()
    win, m_max = player, 0
    for i in temp:
        if temp[0][-1] in str(cards[player]) and i[-1]!=temp[0][-1] or i not in str(cards[player]):
            raise Exception
        cards[player].remove(i)
        if f2(i) > m_max:
            win, m_max = player, f2(i)
        player = next(player)
    return win
try:
    cards=[input().split() for i in range(4)]
    opt=[0 for i in range(4)]
    player,pier,suit=call()
    win=next(player)
    for i in range(3):
        win=pk(cards,win)
        opt[win]+=1
    print('\n'.join(list(map(str,opt))))
    g1 = opt[0]+opt[2]
    g2 = opt[1]+opt[3]
    if pier==3 and (player==0 or player==2):
        print('P1 P3' if g1==3 else 'P2 P4')
    elif pier==3 and (player==1 or player==3):
        print('P1 P3' if g2!=3 else 'P2 P4')
    else:
        print('P1 P3' if g1>g2 else 'P2 P4')
except:
    print('ERROR')