def main(): 
    n=input()
    i=1
    x=''
    if(n.isdigit()==1):
        n=int(n)
        if(n>0 and n%1==0):
            m=(n//2)+1#
            while i<m:
                count=0
                start=i
                j=i+1
                while j<n:
                    if start<n:
                        count+=1
                        start+=j
                        j+=1
                    if start==n:
                        for z in range(i,j):
                            x+=str(z)
                            x=x+'+'
                        x=x.rstrip('+')
                        print(x)
                        break
                    if start>n:
                        break    
                i+=1
                x=''
            print(n)
        else:
            print('E')
    else:
         print('E')
main()    