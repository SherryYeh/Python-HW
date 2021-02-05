#from fractions import Fraction 
n=d=0
def add(n1,d1,n2,d2):
    """x=Fraction(n1,d1)
    y=Fraction(n2,d2)
    i=0
    if(x+y>1):
        i+=1
        s=(x+y)-1*i
        print(str(i)+"("+str(s)+")")
    else:
        print(x+y)"""
    A=abs(n1*d2+n2*d1)
    B=abs(d1*d2)
    min1=min(A,B)   
    for i in range(min1,0,-1):    
        global n,d
        if((n1*d2+n2*d1)%i==0 and d1*d2%i==0):    
            n=(n1*d2+n2*d1)//i
            d=(d1*d2)//i
            break			
        else:
            n=(n1*d2+n2*d1)
            d=(d1*d2)
            if(n<0 and d<0):
                n=-n
                d=-d
    if(abs(n)>abs(d)):
        if (n>d and d>0):
            curry=n//d
            n=n-curry*d
            if(n!=0):
                print(str(curry)+"("+str(n)+"/"+str(d)+")")
            else:
                print(str(curry))
        elif(n>d and d<0):
            curry=n//-d
            n=n+curry*d
            if(n!=0):                
                    print(str(-curry)+"("+str(n)+"/"+str(-d)+")")
            else:
                print(str(-curry))
        elif(d>n and n<0 and d>0):
            curry=-n//d
            n=n+curry*d
            if(n!=0):
                print(str(-curry)+"("+str(-n)+"/"+str(d)+")")
            else:
                print(str(-curry))
        else:
            curry=n//d
            n=n-curry*d
            if(n!=0):
                if(n<0 and d<0):
                    print(str(curry)+"("+str(-n)+"/"+str(-d)+")")
                else:
                    print(str(curry)+"("+str(n)+"/"+str(d)+")")
            else:
                print(str(curry))
    else:
        if(n%d==0):
            print(n//d)
        else:
            if (n>d):
               print(str(-n)+"/"+str(-d))
            else:
                print(str(n)+"/"+str(d))            
n=d=0
def minus(n1,d1,n2,d2):
    A=abs(n1*d2-n2*d1)
    B=abs(d1*d2)
    min1=min(A,B)
    if(A!=0):
        global n,d
        for i in range(min1,0,-1):
            if((n1*d2-n2*d1)%i==0 and d1*d2%i==0):
                n=(n1*d2-n2*d1)//i
                d=(d1*d2)//i
                break			
            else:
                n=(n1*d2-n2*d1)
                d=(d1*d2)
                if(n<0 and d<0):
                    n=-n
                    d=-d
        if(abs(n)>abs(d)):
            if(n>d and d>0):
                curry=n//d
                n=n-curry*d
                if(n!=0):    
                    print(str(curry)+"("+str(n)+"/"+str(d)+")")
                else:
                    print(str(curry))
            elif(n>d and d<0):
                curry=n//-d
                n=n+curry*d
                if(n!=0):
                    print(str(-curry)+"("+str(n)+"/"+str(-d)+")")
                else:
                    print(str(-curry))
            elif(d>n and n<0 and d>0):
                curry=-n//d
                n=n+curry*d
                if(n!=0):
                    print(str(-curry)+"("+str(-n)+"/"+str(d)+")")
                else:
                    print(str(-curry))
            else:
                curry=n//d
                n=n-curry*d
                if(n!=0):
                    if(n<0 and d<0):
                        print(str(curry)+"("+str(-n)+"/"+str(-d)+")")
                    else:
                        print(str(curry)+"("+str(n)+"/"+str(d)+")")
                else:
                    print(str(curry))
        else:
            if(n>d and d<0 and n>0):
                print(str(-n)+"/"+str(-d))
            elif(n>d and d<0 and n<0):
                print(str(-n)+"/"+str(-d))
            elif(n%d==0):
                print(n//d)
            else:
                print(str(n)+"/"+str(d))
    else:
        print("0")	
def multiply(n1,d1,n2,d2):
    if(abs(n1)>abs(d1)):
        for i in range(abs(d1),1,-1):
            if(n1%i==0 and d1%i==0):
                n1=n1//i
                d1=d1//i
                break
    else:
        for i in range(abs(n1),1,-1):
            if(n1%i==0 and d1%i==0):
                n1=n1//i
                d1=d1//i
                break
    if(abs(n2)>abs(d2)):
        for i in range(abs(d2),1,-1):
            if(n2%i==0 and d2%i==0):
                n2=n2//i
                d2=d2//i
                break
    else:
        for i in range(abs(n2),1,-1):
            if(n2%i==0 and d2%i==0):
                n2=n2//i
                d2=d2//i
                break				
    if(abs(n2)>abs(d1)):
        for i in range(abs(d1),1,-1):
            if(n2%i==0 and d1%i==0):
                n2=n2//i
                d1=d1//i
                break
    else:
        for i in range(abs(n2),1,-1):
            if(d1%i==0 and n2%i==0):
                d1=d1//i
                n2=n2//i
                break
    if(abs(d2)>abs(n1)):
        for i in range(abs(n1),1,-1):
            if(d2%i==0 and n1%i==0):
                d2=d2//i
                n1=n1//i
                break
    else:
        for i in range(abs(d2),1,-1):
            if(d1%i==0 and n2%i==0):
                d1=d1//i
                n2=n2//i
                break				
    if(abs(n1*n2)>abs(d1*d2)):        
        if(n1*n2>0 and d1*d2<0): 
            curry=(n1*n2)//(-d1*d2)
            n=(n1*n2)+curry*(d1*d2)
            if(n!=0):
                print(str(-curry)+"("+str(n)+"/"+str(-d1*d2)+")")
            else:
                print(str(-curry))
        elif(n1*n2<0 and d1*d2<0): 
            curry=(-n1*n2)//(-d1*d2)
            n=(-n1*n2)-curry*(-d1*d2)
            if(n!=0):
                print(str(curry)+"("+str(n)+"/"+str(-d1*d2)+")")
            else:			
                print(str(curry))
        else:
            curry=(n1*n2)//(d1*d2)
            n=(n1*n2)-curry*(d1*d2)
            if(n!=0):
               print(str(curry)+"("+str(abs(n))+"/"+str(abs(d1*d2))+")")
            else:			
                print(str(curry))
    else:
        if((n1*n2)%(d1*d2)==0):
            print((n1*n2)//(d1*d2))
        else:
            if(d1*d2<0 and n1*n2>0):
                print(str(-n1*n2)+"/"+str(-d1*d2))
            elif(d1*d2<0 and n1*n2<0):
                print(str(-n1*n2)+"/"+str(-d1*d2))
            else:
                print(str(n1*n2)+"/"+str(d1*d2))	
def divide(n1,d1,n2,d2):
    if(abs(n1)>abs(d1)):
        for i in range(abs(d1),1,-1):
            if(n1%i==0 and d1%i==0):
                n1=n1//i
                d1=d1//i
                break
    else:
        for i in range(abs(n1),1,-1):
            if(n1%i==0 and d1%i==0):
                n1=n1//i
                d1=d1//i
                break
    if(abs(n2)>abs(d2)):
        for i in range(abs(d2),1,-1):
            if(n2%i==0 and d2%i==0):
                n2=n2//i
                d2=d2//i
                break
    else:
        for i in range(abs(n2),1,-1):
            if(n2%i==0 and d2%i==0):
                n2=n2//i
                d2=d2//i
                break
    if(abs(d2)>abs(d1)):
        for i in range(abs(d1),1,-1):
            if(d2%i==0 and d1%i==0):
                d2=d2//i
                d1=d1//i
                break
    else:
        for i in range(abs(d2),1,-1):
            if(d1%i==0 and d2%i==0):
                d1=d1//i
                d2=d2//i
                break
    if(abs(n2)>abs(n1)):
        for i in range(abs(n1),1,-1):
            if(n2%i==0 and n1%i==0):
                n2=n2//i
                n1=n1//i
                break
    else:
        for i in range(abs(n2),1,-1):
            if(n1%i==0 and n2%i==0):
                n1=n1//i
                n2=n2//i
                break
    if(abs(n1*d2)>abs(d1*n2)):
        if(n1*d2>0 and n2*d1<0): 
            curry=(n1*d2)//(-d1*n2)
            n=(n1*d2)+curry*(d1*n2)
            if(n!=0):
                print(str(-curry)+"("+str(n)+"/"+str(-d1*n2)+")")
            else:			
                print(str(-curry))
        elif(n1*d2<0 and n2*d1<0): 
            curry=(-n1*d2)//(-d1*n2)
            n=(-n1*d2)-curry*(-d1*n2)
            if(n!=0):
                print(str(curry)+"("+str(n)+"/"+str(-d1*n2)+")")
            else:			
                print(str(curry))
        else:
            curry=(n1*d2)//(d1*n2)
            n=(n1*d2)-curry*(d1*n2)
            if(n!=0):
                print(str(curry)+"("+str(abs(n))+"/"+str(abs(d1*n2))+")")
            else:			
                print(str(curry))
    else:
        if((n1*n2)%(d1*d2)==0):
                print((n1*d2)//(d1*n2))
        else:
            if(n2*d1<0 and n1*d2>0):
                print(str(-n1*d2)+"/"+str(abs(-d1*n2)))
            elif(n2*d1<0 and n1*d2<0):
                print(str(-n1*d2)+"/"+str(abs(-d1*n2)))
            else:
                print(str(n1*d2)+"/"+str(d1*n2))	
def main():
    x=input().split("/")
    n1=int(x[0])
    d1=int(x[1])
    y=input().split("/")
    n2=int(y[0])
    d2=int(y[1])
    if(n1==0 or d1==0 or n2==0 or d2==0):
        for i in range(4):
            print("ERROR")
    else:
        add(n1,d1,n2,d2)
        minus(n1,d1,n2,d2)
        multiply(n1,d1,n2,d2)
        divide(n1,d1,n2,d2)
main()