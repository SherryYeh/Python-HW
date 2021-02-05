def triangle(a,b,c):
    if (a+b<=c or b+c<=a or c+a<=b or a<=0 or b<=0 or c<=0):
	    return 1        
    if a==b==c:
        return 2    
    if a==b and (a**2+b**2)>(c**2) or b==c and (c**2+b**2)>(a**2) or c==a and (a**2+c**2)>(b**2):
        return 3
def output(triangle):
    if (triangle==1):
        print('not triangle')
    elif (triangle==2):
        print('equilateral triangle')
    elif (triangle==3):
        print('isosceles triangle')
    else:
        print('triangle')
def main():
    x=input().split(.)
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    """a,b,c=input().split()#兩種都行
    a=int(a)
    b=int(b)
    c=int(c)"""
    """t=triangle(a,b,c)
	output(t)"""
    output(triangle(a,b,c))
main()