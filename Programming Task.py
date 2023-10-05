#!/usr/bin/env python
# coding: utf-8

#  Task1 : Calculate Area with Conditions
# 

# In[1]:


def calculate_area(a,b):
    if a == b :
        return "This is a Square"
    else:
        return a*b

Length = int(input("Enter the length: "))
Width  = int(input("Enter the width: "))
calculate_area(Length,Width)
    


#  Task2 : Generate Fibonacci series

# In[18]:


def fibonacci(n):
    f = [0,1]
    for i in range(2,n):
        f.append(f[i-1] + f[i-2])
        
    return f

x = int(input("Enter the number: "))
fibonacci(x)


# In[ ]:




