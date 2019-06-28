#!/usr/bin/env python
# coding: utf-8

# In[1]:


pi = 3.14
r = float(input("Enter radius"))
a = pi*r*r
print(a)


# In[4]:


a = int(input("Enter a number"))
if a > 0:
    print("the number is positive")
elif a < 0:
    print("The number is negative")
else :
    print("the number is zero")


# In[5]:


a = int(input("Enter a number"))
b = int(input("Enter another number"))
c= a%b
if c==0:
    print("the numbers are divisible")
else :
    print("Numbers are not divisible")


# In[6]:


pi = 3.14
r = float(input("Enter radius"))
v = 4*pi*r*r*r/3
print(v)


# In[10]:


a = input("Enter a string")
b = int(input("Enter how many times do you want it copied"))
x =0
while x != b:
    print(a)
    x= x+1


# In[11]:


a = int(input("Enter a number"))
if a%2 ==0:
    print("number is even")
else :
    print("number is odd")


# In[10]:


import sys
a = ['a' , 'e' , 'i' , 'o' , 'u' ]
v = input("Enter a string")
c= 0
for x in a:
    if x == v:
        c = "y"
if c=="y":
    print("this is a vowel")
else:
    print("this isn't a vowel")

        
        
    


# In[11]:


b = float(input("Enter base of triangle"))
h = float(input("Enter height of triangle"))
a = 0.5*b*h
print(a)


# In[12]:


p = float(input("Enter principle amount"))
r = float(input("Enter rate of interest"))
y = float(input("Enter number of years"))
f = p*(1+r)**y
print(f)


# In[13]:


import math
x1 = float(input("enter x1 co-ordinate"))
x2 = float(input("enter x2 co ordinate"))
y1 = float(input("enter y1 co ordinate"))
y2 = float(input("enter y2 co ordinate"))
d1 = x1 - x2
d1 = d1**2
d2 = y1 - y2
d2 = d2**2
f = math.sqrt(d1+d2)
print(f)


# In[14]:


a = float(input("Enter height in feet"))
c = a*30.48
print(c)


# In[16]:


w = float(input("enter weight in kgs"))
h = float(input("enter height in ms"))
bmi = w/(h**2)
print(bmi)


# In[19]:


sum = 0
n = int(input("enter number till which sum is required"))
for x in range(n+1):
    sum = sum + x
print(sum)    


# In[28]:


a = []
b = []
n=0
m=0
while n <3:
    a.append(int(input("enter final date in dd/mm/yyyy format")))
    n=n+1
while m <3:
    b.append(int(input("enter inital date in dd/mm/yyyy format")))
    m=m+1   
y = (a[2]-b[2])*365
m = (a[1]-b[1])*30
d = a[0]-b[0]
total = d+y+m
print(total)


# In[ ]:




