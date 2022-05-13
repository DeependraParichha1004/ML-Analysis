#MINI CALCULATOR
print("welcome to mini calculator")
print("enter a number")
inpnum1=int(input())
print("enter a number")
inpnum2=int(input())
print("what is your operator ",'+','-','*','/')
operator=input()
answer="your answer is"
if inpnum1==56 and inpnum2==6 and operator=='/':
    print('100')
elif inpnum1==56 and inpnum2==9 and operator=='+':
    print('77')
elif inpnum1==45 and inpnum2==3 and operator=='*':
    print('555')
elif operator=='+':
    sum=inpnum1+inpnum2
    print(answer,sum)
elif operator=='-':
    difference=inpnum1-inpnum2
    print(answer,difference)
elif operator=='*':
    multiplication=inpnum1*inpnum2
    print(answer,multiplication)
elif operator=='/':
    division=inpnum1/inpnum2
    print(answer,division)
else:
    print("fuck off,apna dimag mat laga,jitna operator ke option mein hai unmeinse.")
exit();


