def main():##主程式
    n1=list(map(int,input().split('/')))
    n2=list(map(int,input().split('/')))
    if 0 in n1 or 0 in n2:##測試
        for i in range(4):
            print('ERROR')
    else:
        addans1,addans2,x,signadd=addfunction(n1,n2)
        minans1,minans2,y,signmin=minus(n1,n2)
        mulans1,mulans2,z,signmul=multiply(n1,n2)
        divans1,divans2,q,signdiv=divied(n1,n2)
        output(addans1,addans2,x,signadd)
        output(minans1,minans2,y,signmin)
        output(mulans1,mulans2,z,signmul)
        output(divans1,divans2,q,signdiv)
def addfunction(n1,n2):##加法
    ans1=n1[0]*n2[1]+n1[1]*n2[0]
    ans2=n1[1]*n2[1]
    ans1,ans2,testadd=absolute(ans1,ans2)
    ans1,ans2=math(ans1,ans2)
    ans1,ans2,x=math2(ans1,ans2)
    return ans1,ans2,x,testadd
def minus(n1,n2):##減法
    ans1=n1[0]*n2[1]-n1[1]*n2[0]
    ans2=n1[1]*n2[1]
    ans1,ans2,testmin=absolute(ans1,ans2)
    ans1,ans2=math(ans1,ans2)
    ans1,ans2,y=math2(ans1,ans2)
    return ans1,ans2,y,testmin
def multiply(n1,n2):##乘法
    ans1=n1[0]*n2[0]
    ans2=n1[1]*n2[1]
    ans1,ans2,testmul=absolute(ans1,ans2)
    ans1,ans2=math(ans1,ans2)
    ans1,ans2,z=math2(ans1,ans2)
    return ans1,ans2,z,testmul
def divied(n1,n2):##除法
    ans1=n1[0]*n2[1]
    ans2=n1[1]*n2[0]
    ans1,ans2,testdiv=absolute(ans1,ans2)
    ans1,ans2=math(ans1,ans2)
    ans1,ans2,q=math2(ans1,ans2)
    return ans1,ans2,q,testdiv
def math(ans1,ans2):##最簡分數
    for i in range(ans1,0,-1):
        if ans1%i==0 and ans2%i==0:
            ans2=ans2//i
            ans1=ans1//i
            break
    return ans1,ans2
def math2(ans1,ans2):##整數部分
    if(ans1>=ans2):
        x=ans1//ans2
        ans1=ans1%ans2
        return ans1,ans2,x
    else:
        return ans1,ans2,0
def absolute(ans1,ans2):##判斷正負
    sign=0
    if ans1<0:
        ans1=abs(ans1)
        sign+=1
    if ans2<0:
        ans2=abs(ans2)
        sign+=1
    return ans1,ans2,sign
def output(a,b,x,s):##輸出
    if x==0:
        if a==0:
            print(x)
        else:
            if s==1:
                print('-%d/%d'%(a,b))
            else:
                print('%d/%d'%(a,b))
    else:
        if a==0:
            if s==1:
                print('-%d'%x)
            else:
                print(x)
        else:
            if s==1:
                print('-%d(%d/%d)'%(x,a,b))
            else:
                print('%d(%d/%d)'%(x,a,b))
main()