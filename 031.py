def compute(one):
    if one[0].isdigit()==True:
        if one.isdigit()!=True:
            return "Invalid"            
        else:
            return "Number"
    else:
        if(judge(one)=="Y"):
            return "Invalid"
        elif(judge(one)=="N"):
            return "Identifier"       
def judge(one):
    for j in range(1,len(one)):
        if one[j].isdigit()!=True and one[j]!="_" and not("A"<=one[j]<="Z") and not("a"<=one[j]<="z"):
            return "Y"
    return "N"  
def main():
    while(True):
        list1=input().split()
        if("." in list1):
            break
    for i in range(len(list1)-1):
        ANS=compute(list1[i])
        print("%s - %s"%(list1[i],ANS))
main()