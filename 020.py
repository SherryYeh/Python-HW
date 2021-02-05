def transfer(a,b):
    if(1<a<17):
        list=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        result=""
        while(b>0):
            num=b%a
            b//=a
            result+=list[num]       
        print(result[::-1])
        """result=list[num]+result
		print(result)"""
    else:
        print("E")
def main():
    a,b=input().split()
    a=int(a)
    b=int(b)
    transfer(a,b)
main()