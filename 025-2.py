def inputfunction():
    play1=list(map(int,input().split()))
    play2=list(map(int,input().split()))
    return play1,play2
def main():
    play1,play2=inputfunction()
    if play1[0]==10:
        ANS=strike(play1,play2)
    elif play1[0]+play1[1]==10:
        ANS=spare(play1,play2)
    else:
        if play2[0]+play2[1]==10:
            ANS=play1[0]+play1[1]+play2[0]+play2[1]+play2[2]+play2[3]
        else:
            ANS=play1[0]+play1[1]+play2[0]+play2[1]
    output(ANS)
def strike(play1,play2):
    if play2[0]==10:
        ANS=play1[0]+((play2[0]+play2[2])*2)+play2[3]
    elif play2[0]+play2[1]==10:
        ANS=play1[0]+((play2[0]+play2[1])*2)+play2[2]+play2[3]
    else:
        ANS=play1[0]+((play2[0]+play2[1])*2)
    return ANS
def spare(play1,play2):
    if play2[0]==10:
        ANS=play1[0]+play1[1]+(play2[0]*2)+play2[2]+play2[3]
    elif play2[0]+play2[1]==10:
        ANS=play1[0]+play1[1]+(play2[0]*2)+play2[1]+play2[2]+play2[3]
    else:
        ANS=play1[0]+play1[1]+(play2[0]*2)+play2[1]
    return ANS
def output(ANS):
    print(ANS)
main()