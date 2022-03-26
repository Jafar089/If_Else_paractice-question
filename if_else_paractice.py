#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[3]:


num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
if num1>num2:
    print(num1,' is grater and ',num2,' is smaller')
else:
    print(num2,' is grater and ',num1,' is smaller')


# # Question 2

# In[4]:


x=int(input("Enter number between 1 to 10: "))
while x<1 or x>10:
    print('plz enter number between 1 to 10')
    x=int(input("Enter first number: "))
romen=['I','II','III','IV','V','VI','VII','VIII','IX','X']
print(romen[x-1])


# # Question 3

# In[5]:


day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter a year: '))

if day*month == year:
    print("The date is magic.")
else:
    print("The date is not magic.")


# # Question 4

# In[6]:


length1 = int(input('Enter length no 1: '))
width1 = int(input('Enter width no 1: '))
length2 = int(input('Enter length no 2: '))
width2 = int(input('Enter width no 2: '))

area1 = length1*width1
area2 = length2*width2

if area1>area2:
    print('Rectangle 1 has greater area...')
elif area1==area2:
    print('Both have same area...')
else:
    print('Rectangle no 2 has greater area...')


# # Question 5

# In[7]:


i = int(input('how many books you purchased: '))
if i == 0:
    print('0 points are awarded...')
elif i == 1:
    print('5 points are awarded...')
elif i == 2:
    print('15 points are awarded...')
elif i == 3:
    print('30 points are awarded...')
elif i >= 4:
    print('60 points are awarded...')
else:
    print('wrong input...')


# # Question 6

# In[48]:


mass=int(input('Enter mass of an object: '))
weight = mass*9.8

if weight>= 1000:
    print('It is too heavy.')
elif weight>0 and weight<=9:
    print('The object is too light.')


# # Question 7

# In[44]:


sec=int(input('Enter number of seconds: '))

if sec >=86400:
    print('There are ',sec/86400,' days in that seconds')
elif sec>=3600 and sec<86400:
    print('There are ',sec/3600,' hours in that seconds')
elif sec>=60 and sec<3600:
    print('There are ',sec/60,' minutes in that seconds')


# # Question 8

# In[60]:


from random import randint
num1 = randint(0, 100)
num2 = randint(0, 100)
sum=num1+num2
print(' ',num1)
print('+',num2)

student=int(input('Enter answer of that question: '))

if student == sum:
    print('Congratulations')
else:
    print(' You are wrong \n',sum, ' is a correct answer')


# # Question 9

# In[75]:


units=int(input('How many units you have to purchased: '))
price = 99
cal20=(price*units)/100*20
cal30=(price*units)/100*30
cal40=(price*units)/100*40
cal50=(price*units)/100*50
if units>0 and units<=9:
    print('No discount your total price is $',price*units)
elif units>=10 and units<=19:
    print('After discount of 20% your total is: &',price*units-cal20)
elif units>=20 and units<=49:
    print('After discount of 30% your total is: &',price*units-cal30)
elif units>=50 and units<=99:
    print('After discount of 40% your total is: &',price*units-cal40)
elif units>=100:
    print('After discount of 50% your total is: &',price*units-cal50)


# # Question 10

# In[76]:


checks = int(input('Enter no of checks: '))
while checks<=0:
    checks = int(input('Plz enter checks greater than 0: '))

if checks>0 and checks<=19:
    print('The bank fees is $10')
elif checks>=20 and checks<=39:
    print('The bank fees is $.08')
elif checks>=40 and checks<=59:
    print('The bank fees is $.06')
else:
    print('The bank fees is $.04')


# # Question 11

# In[8]:


pie=3.14156
choice=int(input('''Enter 1 for Calculate the Area of a Circle 
Enter 2 for Calculate the Area of a Rectangle
Enter 3 for Calculate the Area of a Triangle
Enter 4 for quit the program'''))
if choice == 1:
    radius=int(input('Enter radius: '))
    print('Area of a Circle is: ',pie*radius**2)
elif choice == 2:
    length=int(input('Enter length of a rectangle: '))
    width=int(input('Enter width of a rectangle: '))
    print('Area of a Rectangle is: ',length*width)
elif choice == 3:
    height=int(input('Enter height of triangle: '))
    base=int(input('Enter base of triangle: '))
    print('Area of a triangle is: ',base*height/2)
elif choice == 4:
    print('Quit..!')


# # Question 12

# In[10]:


runner1=input("Enter name of nunner no 1: ")
runner2=input("Enter name of nunner no 2: ")
runner3=input("Enter name of nunner no 3: ")
time1=int(input("Enter time of "+runner1))
while time1<0:
    time1=int(input("plz Enter time in positive integers of "+runner1))
time2=int(input("Enter time of "+runner2))
while time2<0:
    time2=int(input("plz Enter time in positive integers of "+runner2))
time3=int(input("Enter time of "+runner3))
while time3<0:
    time3=int(input("plz Enter time in positive integers of "+runner3))


# first time 1

if time1<time2 and time1<time3:
    print(runner1,' take first position.')
    if time2<time3:
        print(runner2,' take second position.')
        print(runner3,' take third position.')
    else:
        print(runner3,' take second position.')
        print(runner2,' take third position.')
        
elif time1<time2 and time1>time3:
    print(runner3,' take first position.')
    print(runner1,' take second position.')
    print(runner2,' take third position.')
    

elif time1>time2 and time1<time3:
    print(runner2,' take first position.')
    print(runner1,' take second position.')
    print(runner3,' take third position.')
    
    
elif time1>time2 and time1>time3:
    print(runner1,' take third position.')
    if time2<time3:
        print(runner2,' take first position.')
        print(runner3,' take second position.')
    else:
        print(runner3,' take first position.')
        print(runner2,' take second position.')
    
#second time 2

elif time2<time1 and time2<time3:
    print(runner2,' take first position.')
    if time1<time3:
        print(runner1,' take second position.')
        print(runner3,' take third position.')
    else:
        print(runner3,' take second position.')
        print(runner1,' take third position.')
        
elif time2<time1 and time2>time3:
    print(runner3,' take first position.')
    print(runner2,' take second position.')
    print(runner1,' take third position.')
    

elif time2>time1 and time2<time3:
    print(runner1,' take first position.')
    print(runner2,' take second position.')
    print(runner3,' take third position.')
    
    
elif time2>time1 and time2>time3:
    print(runner2,' take third position.')
    if time1<time3:
        print(runner1,' take first position.')
        print(runner3,' take second position.')
    else:
        print(runner3,' take first position.')
        print(runner1,' take second position.')

# third time 3

elif time3<time1 and time3<time2:
    print(runner3,' take first position.')
    if time1<time2:
        print(runner1,' take second position.')
        print(runner2,' take third position.')
    else:
        print(runner2,' take second position.')
        print(runner1,' take third position.')
        
elif time3<time1 and time3>time2:
    print(runner2,' take first position.')
    print(runner3,' take second position.')
    print(runner1,' take third position.')
    

elif time3>time1 and time3<time2:
    print(runner1,' take first position.')
    print(runner3,' take second position.')
    print(runner2,' take third position.')
    
    
elif time3>time1 and time3>time2:
    print(runner3,' take third position.')
    if time1<time2:
        print(runner1,' take first position.')
        print(runner2,' take second position.')
    else:
        print(runner2,' take first position.')
        print(runner1,' take second position.')

