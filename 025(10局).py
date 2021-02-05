def main():
    ANS=0
    play=[]
    for i in range(10):
        play.append(list(map(int,input().split())))
    for i in range(9):
        if play[i][0]==10:
            ANS+=strike(play,i)
        elif play[i][0]+play[i][1]==10:	
            ANS+=spare(play,i)
        else:
            ANS+=play[i][0]+play[i][1]
            if i==8 and play[9][0]+play[9][1]!=10:
                ANS+=play[9][0]+play[9][1]
            elif i==8:
                ANS+=10+play[9][2]+play[9][3]
    print(ANS)
def strike(play,i):
    if i<=7:
        if play[i+1][0]==10:
            ANS=10+play[i+1][0]+play[i+2][0]
        else:
            ANS=10+play[i+1][0]+play[i+1][1]
    if i==8:
        if play[9][0]==10:
            ANS=10+(play[9][0]+play[9][2])*2+play[9][3]
        elif play[9][0]+play[9][1]==10:
            ANS=10+(play[9][0]+play[9][1])*2+play[9][2]
        else:
            ANS=10+(play[9][0]+play[9][1])*2
    return ANS
def spare(play,i):
    if i<=7:
        ANS=10+play[i+1][0]            
    if i==8:
        if play[9][0]==10:
            ANS=10+play[9][0]*2+play[9][2]+play[9][3]
        elif play[9][0]+play[9][1]==10:
            ANS=10+play[9][0]*2+play[9][1]+play[9][2]
        else:
            ANS=10+play[9][0]*2+play[9][1]
    return ANS
main()