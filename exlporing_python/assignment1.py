# ##problem_1:
value=int(input("enter the value= "))
if value%2==0:
    print(f"{value} is an even number")
else:
    print(f"{value}is an odd number")

##problem_2:
number_1,number_2=map(int,input("enter number_1 & number_2=").split())
operator=(input("type the operator="))
if operator=='+':
    print(f"{number_1}+{number_2}=",number_1+number_2)
elif operator=='-':
    print(f"{number_1}-{number_2}=",number_1-number_2)
elif operator=='*':
    print(f"{number_1}*{number_2}=",number_1*number_2)
elif operator=='/':
    if number_2 !=0:
     print(f"{number_1}/{number_2}=",number_1/number_2)
    else:
        print("error")
else:
    print("invalid operator")


##problem_3.:
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i

print(sum)