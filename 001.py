def computerScore(chinese,csi,pd):
    average=(chinese+csi+pd)//3
    total=(chinese+csi+pd)
    return average,total
def main():
    name=input()
    id=int(input())
    chinese=int(input())
    csi=int(input())
    pd=int(input())
    average,total=computerScore(chinese,csi,pd)
    print("Name:%s"%name)
    print("ID:%d"%id)
    print("Average:%d"%average)
    print("Total:%d"%total)
main()    
    
    

