dict1 = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}

def NextPlayer(player):
    if(player == 3):
        return 0
    else:
        return player + 1

def ConvertCardA(card):#把牌變成4A -> 414 , 5A->405 這種形式
    rank = int(card.replace(card[-1], ""))
    if(rank == 1):rank = 14
    suit = dict1[card[-1]]
    return suit * 100 + rank

def ConvertCardB(card):
    rank = int(card.replace(card[-1], ""))
    suit = dict1[card[-1]]
    return rank * 10 + suit

def vs(cards,play):
    tmp=input().split()
    win,maxcard=play,0
    for i in tmp:
        if tmp[0][-1] in str(cards[play]) and i[-1]!=tmp[0][-1] or i not in str(cards[play]):#如果玩家明明可以跟出同樣的花色但她卻出別張牌 或是他出自己手中明明沒這張牌但她卻生出來
            raise Exception#拋出例外
        cards[play].remove(i)#出過得牌要移除
        if ConvertCardA(i)>maxcard:#如果這張是目前最大的那就刷新資訊
            win,maxcard=play,ConvertCardA(i)
        play=NextPlayer(play)
    return win

def saycard():
    PassCount = Point = winPlayer = 0
    Player = -1
    Suit = "E"
    while(True):
        Player = NextPlayer(Player)
        tmp = input()
        if(tmp == "pass"):
            PassCount += 1
        else:
            PassCount = 0
            if(ConvertCardB(tmp) > Point and  ConvertCardB(tmp) < 40):#若目前叫牌比之前的還大 且沒超過3敦的範圍
                Point = ConvertCardB(tmp)
                Suit = tmp[-1]
                winPlayer = Player
            else:
                raise Exception
        if(PassCount == 3):
            return winPlayer, Point//10, Suit
        
def main():
    try:
        cards = [input().split() for i in range(4)]
        result = [0 for i in range(4)]
        player, Point, Suit = saycard()
        dict1[Suit] = 5

        win = NextPlayer(player)
        for i in range(3):
            win = vs(cards, win)
            result[win] += 1
        print('\n'.join(list(map(str, result))))
        team1, team2 = result[0] + result [2], result[1] + result[3]
        if(Point== 3 and (player == 0 or player == 2)):
            if(team1 == 3):
                print("P1 P3")
            else:
                print("P2 P4")
        elif(Point == 3 and (player == 1 or player == 3)):
            if(team2 == 3):
                print("P2 P4")
            else:
                print("P1 P3")
        else:
            if(team1 > team2):
                print("P1 P3")
            else:
                print("P2 P4")
    except:
        print("ERROR")

main()