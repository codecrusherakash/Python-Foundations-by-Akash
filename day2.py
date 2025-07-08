#grade calculator
mark=int(input("Enter the marks out of 100:"))
if(mark<0 or mark>100):
    print("The marks entered is Invalid")
elif(mark>=90):
    print("Excellent, your grade is A+")
elif(mark>=80):
    print("Awesome, your grade is A")
elif(mark>=70):
    print("congratulations your grade is B")
elif(mark>=60):
    print("you made it good,your grade is C")
elif(mark>=50):
    print("You Did well,your  grade is D")
else:
    print("Failed Sorry, try next time but don't lose hope your grade is 'F' ")

#body  mass index calculator
weight=float(input("Enter weight of the person(in kgs):"))
height=float(input("Enter the height of the person(in meters):"))
bmi=weight/(height**2)
if(bmi<18.5):
    print("Category:Underweight")
elif(18.5<bmi<25):
    print("Category:Normal")
elif(25<=bmi<30):
    print("Category:Overweight")
elif(30<bmi):
    print("Category:You are an Obesity patient,take care of your body please.")

#Atm cash withdrawal
balance=10000
print(f"The balance remaining in your Bank Account is:{balance}")
cash=float(input("Enter the amount you want to withdraw:"))
if(0>cash or cash>balance):
    print("Invalid Amount Entered")
else:
    if(cash % 100 !=0):
        print("Please enter withdrawal amount in multiples of 100")
    else:
        taken=balance-cash
        print(f"The Money of Rs.{cash} has been withdrawn by the user and remaining balance is Rs.{taken}")

#programs:
#1)
marks=int(input("Enter Marks:"))
if(marks>=90):
    print("Outstanding and your grade is 'A+'")
elif(marks>=80):
    print("Excellent and your grade is 'A'")
elif(marks>=70):
    print("Good job and your grade is 'B'")
elif(60<=marks):
    print("Needs Improvement and your grade is 'C'")
elif(50<=marks):
    print("Needs critical Improvement and your grade is 'D'")
else:
    print("Fail,Try Next time")
#2)
age=int(input("Enter your Age:"))
if(age<=0):
    print("Invalid Age Range")
elif(12>=age>0):
    print("Hello Kiddo,You're welcome")
elif(19>=age>=13):
    print("Hello Teen,You're at best part of your life learn everything possible in this age ok")
elif(59>=age>=20):
    print("You are the one's building the world,nice meeting you")
elif(age>=60):
    print("You are the one's who  survived in this storm called world,it is honour to meet you.")

#3)
print("This is  to check whether entered year is leap year or not")
year=int(input("Enter the year:"))
if(year % 4 ==0):
    print(f"{year} is a leap year,You got more days to work")
else:
    print(f"{year} is not a leap year,but still you have to keep grinding")

#4)
print("The rates applied on each unit is displayed as follows \n 0 to 100 -Rs.1.5 \n 101 to 200 - Rs.2.5 \n 201 to 300 - Rs.4 \n above 300 - Rs.6\n")
units=int(input("Enter the number of units consumed:"))
billamount=0
if(units<0):
    print("Invalid units value")
elif(units==0):
    print("Oh! God ,How do  you even survive whithout electricity")
elif(0<units<=100):
    billamount+=1.5*units
    print(f"The billamount after consuming {units} is {billamount}")
elif(101<=units<=200):
    billamount+=2.5*units
    print(f"The billamount after consuming {units} is {billamount}")
elif(201<=units<=300):
    billamount+=4*units
    print(f"The billamount after consuming {units} is {billamount}")
elif(units>300):
    billamount+=6*units
    print(f"The billamount after consuming {units} is {billamount}")


#5)
income=float(input("Enter your income(in rupees and in numbers):"))
if(income<=0):
    print("Dont know how to earn or just don't want to reveal🤔")
else:    
    if(0<income<=250000):
        net1=income
        print(f"After including '0%' tax the net amount will be {net1}")
    elif(income>250000 and income<=500000):
        amount=income-250000
        tax=(amount/100)*5
        net2=income-tax
        print(f"After including  tax i.e,{tax} ,the net amount will be {net2} ")
    elif(income>500000 and income<=1000000):
        amount=income-500000
        tax1=12500
        tax2=(amount/100)*20
        net3=income-(tax1+tax2)
        print(f"After including tax i.e,{tax1+tax2} ,the net amount will be:{net3} ")
    elif(income>1000000):
        amount=income-1000000
        tax1=12500
        tax2=100000
        tax3=(amount/100)*30
        net4=income-(tax1+tax2+tax3)
        print(f"After including tax i.e,{tax1+tax2+tax3} ,the net amount will be {net4} ")