def judge(i):
    x = i.replace('_','')
    if(x[0].isdigit()):
        if(x.isdigit()and i[1:].count('_')==0):
            print('%s - Number'%i)
        else:
            print('%s - Invalid'%i)
    elif(x[0].isalpha() and x.isalnum()):
        print('%s - Identifier'%i)
    else:
        print('%s - Invalid'%i)
def main():
    x = input().split()
    for i in x:
        if(i=='.'):
            break
        judge(i)
main()