def print1(n):
    for i in range(n):
       print("#",end="")
def print2(n):
    for j in range(n,0,-1):
       print(j,end="")    
def main():
    n=int(input())
    for  k in range(n):
        print1(n+k)
        print2(n-k)
        print("")
main()