num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
opr=input("Enter the operation to be performed (add,sub,mul,div):")
result=0
if (opr=="add"):
    result=num1+num2
    print (result)
elif (opr=="sub"):
    result=num1-num2
    print (result)
elif(opr=="mul"):
    result=num1*num2
    print (result)
elif(opr=="div"):
    result=num1/num2 
    print (result)
