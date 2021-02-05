import math
def main(num1,num2):
    difference=abs(num1-num2)
    sum=(num1)+(num2)
    quotient=(num1)/(num2)
    product=(num1)*(num2)
    return difference,sum,quotient,product
num1=int(input())
num2=int(input())
difference,sum,quotient,product=main(num1,num2)
print("Difference:%.2f"%difference)
print("Sum:%.2f" %sum)
print("Quotient:%.2f" %quotient)
print("Product:%.2f" %product) 

