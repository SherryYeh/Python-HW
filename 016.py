def compute(n):
    for k in range(n,2*n,1):
        for j in range(n):
            print("#",end='')
        for i in range(n,0,-1):
            print(i,end='')
        print("\n")
def main():
    n=int(input())
    compute(n)
main()