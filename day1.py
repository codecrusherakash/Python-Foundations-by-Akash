name=input('Enter your name:')
age=input('Enter your age:')
print(f"Hi,{name},you are {age}years old right!")
#subprogram1
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
sum=num1+num2
print(f'The sum is {sum}')
#subprogram2
pi=3.14
a=float(input('Enter the radius'))
res=pi*a*a
print(f"The Area of circle is,{res}")
#sub program 4
l=int(input('Enter length of rectangle'))
b=int(input('Enter bredth of rectangle'))
area=l*b
perimeter=2*(l+b)
print(f'The perimeter of rectangle is{perimeter} and area of rectangle is {area}')
#sub program 5
read=int(input('Enter a number to check even or odd:'))
if(read % 2==0):
    print(f'The {read} is a even number')
else:
    print(f'The {read} is a odd number')

#Basic task1:Simple calculator:
num1=int(input("Enter first number:"))
num2=int(input('Enter second number:'))
print("Sum of numbers is:",num1+num2)
print("Difference of numbers is:",num1-num2)
print("Product of numbers is:",num1*num2)
if (num2!=0):
    print("quotient of numbers is:",num1/num2)
    print("Remainder of numbers is:",num1%num2)
else:
    print("Invalid number is provided for division")


#basic task2:To check whether a number is positive or negative

num=int(input('Enter a number to check whether a number is positive or negative:'))
if(num>0):
    print("Given Value is a positive number")
elif(num<0):
    print("Given Value is a negative number")
elif(num==0):
    print("Given value is zero")

#basic task 3:To find cube of a number

num=int(input("Enter a number to find cube of it:"))
res=num**3
print(f"The cube of {num} is:{res}")

#basic task 4:Print "fizz" if a number is divisible by 3.
# "buzz" if number is divisible by 5 
# else print "fizzbuzz" if number is divisible by both 5 and 3
#if not divisible by both 5 and 3 print apology statement by returning the provided number
num=int(input("Enter a number:"))
if(num % 5==0 and num % 3==0):
    print("Fizzbuzz")
elif(num % 5 ==0):
    print("Buzz")
elif(num %3==0):
    print("Fizz")
else:
    print(f"Sorry,Provided Number {num} is not divisible by both 5 and 3")

#problems:
#1)
print('Finding the largest among two number \n')
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    print(f"{a} is the largest one")
elif(b>a):
    print(f"{b} is the largest one")
elif(a==b):
    print(f"{a,b} both are equal")


#2)

num=int(input('Enter a number to check divisibility by 7 and 11:'))
if(num % 7 == 0 and num % 11 == 0):
    print(f"{num} is divisible by both")
elif(num % 7==0):
    print(f"{num} is divisible by 7")
elif(num % 11==0):
    print(f"{num} is divisible by 11")
else:
    print(f"The number is not divisibble by either of them")

#3)
print("This is for simple intrest")
p=int(input("Enter principal amount:"))
t=float(input("Enter the time of invest(In year):"))
r=int(input("Enter the rate of intrest:"))
si=(p*t*r)/100
print(f"The Simple Intrest will be:{si}")

#4)

name=input("Enter your name:")
age=int(input("Enter your age(in years):"))
if(age<0):
    print("Invalid age")
elif(age>0 and age<18):
    print(f"{name},Sorry! but you are not enough old to vote")
elif(age>=18):
    print(f"{name},you are Eligible to vote")

#5)

billamount=int(input("Enter the billamount:"))
dayslate=int(input("Enter the days late(in numbers):"))
if(dayslate==0):
    print(f"The Billamount will be {billamount}")
elif(dayslate<0):
    print("Invalid delay days")
elif(dayslate>=1 and dayslate<=5):
    fine=5*dayslate
    billamount+=fine
    print(f"The billamount will be{billamount}")
elif(dayslate>=6 and dayslate<=10):
    fine=10*dayslate
    billamount+=fine
    print(f"The billamount will be{billamount}")
elif(dayslate>10):
    print("Sorry!,but your Connection has been disconnected due to delay in payment of bills")
