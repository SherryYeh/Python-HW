def void_f1(x1,y1,x2,y2):
    if(x1 == x2):
        print('x=%d'%(x1))
        print('x=%d'%(x1))
    else:
        m = (y1-y2)/(x1-x2)
        m_son = (y1-y2)
        m_mom = (x1-x2)
        b = (x2*y1-x1*y2)/(x2-x1)
        b_son = (x2*y1-x1*y2)
        b_mom = (x2-x1)
        if(y1 == y2):
            print('y=%d'%(b))
            print('y=%d'%(b))
        else:
            if(m%1 == 0):
                if(b%1 == 0):
                    if(m == 1):
                        print('y=x%+d'%b)
                        print('y=x%+d'%b)
                    elif(m == -1):
                        print('y=-x%+d'%b)
                        print('y=-x%+d'%b)
                    else:
                        print('y=%dx%+d'%(m,b))
                        print('y=%dx%+d'%(m,b))      
                else:
                    print('y=%dx%+.2f'%(m,b))
                    if((b_son<0 and b_mom<0) or (b_son>0 and b_mom<0)):
                        b_son *=-1
                        b_mom *=-1
                    print('y=%dx%+d/%d'%(m,b_son,b_mom))
            else:
                if((m_son<0 and m_mom<0) or (m_son>0 and m_mom<0)):
                    m_son *=-1
                    m_mom *=-1
                if(b%1 == 0):
                    print('y=%.2fx%+d'%(m,b))
                    print('y=%d/%dx%+d'%(m_son,m_mom,b))
                else:
                    if((b_son<0 and b_mom<0) or (b_son>0 and b_mom<0)):
                        b_son *=-1
                        b_mom *=-1
                    print('y=%.2fx%+.2f'%(m,b))
                    print('y=%d/%dx%+d/%d'%(m_son,m_mom,b_son,b_mom))
def main():
    inin = input().split()
    judge = []
    if(len(inin)!=4):
        print('Error!')
    else:
        for i in range(4):
            judge.append(inin[i])
        float = 0
        for i in range(4):
            if(judge[i].startswith('-')):
                #print(judge[i])
                judge[i] = judge[i][1:]
        for i in range(4):
            if(judge[i].count('.')!=0)or(not(judge[i].isdigit())):
                float = 1
        if(float == 1):
            print('Error!')      
        elif(float == 0):
            x1,y1,x2,y2 = int(inin[0]),int(inin[1]),int(inin[2]),int(inin[3])
            void_f1(x1,y1,x2,y2)
main()