def one(b):
    for i in range(1,b+1):
        if(i<=(b+1)//2):
            for j in range(i):
                print("*",end="")
        else:
            for j in range(b+1-i):
                print("*",end="")
        print()
def two(b):
    for i in range(1,b+1):
        if(i<=(b+1)//2):
            for j in range((b+1)//2-i):
                print(".",end="")
            for j in range(i):
                print("*",end="")
        else:
            for j in range(i-(b+1)//2):
                print(".",end="")
            for j in range(b+1-i):
                print("*",end="")
        print()
def three(b):
    for i in range(1,b+1):
        if(i<=(b+1)//2):
            for j in range((b+1)//2-i):
                print(".",end="")
            for j in range(i*2-1):
                print("*",end="")
        else:
            for j in range(i-(b+1)//2):
                print(".",end="")
            for j in range((b+1-i)*2-1):
                print("*",end="")
        print()
def main():
    a=int(input())
    b=int(input())
    if(a==1):
	    one(b)
    elif(a==2):
	    two(b)
    else:
	    three(b)
main()