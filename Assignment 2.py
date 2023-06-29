#!/usr/bin/env python
# coding: utf-8

# ## Q1.What are the two values of the Boolean data type? How do you write them?

# sol.1 : Two type of boolean True and False. 
# We should write them using capital T and F, with the rest of the word in lowercase.
# True 
# False

# ## Q2. What are the three different types of Boolean operators?

#  Sol.2: Three different types of Boolean operators are and, or ,and not. 

# ## Q3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
Sol3.  True and True is True.
       True and False is False.
       False and True is False.
       False and False is False.
       True or True is True.
       True or False is True.
       False or True is True.
       False or False is False.
       not True is False.
       not False is True.
# ## Q4. What are the values of the following expressions?

# In[5]:


not ((5 > 4) or (3 == 5))


# In[3]:


not (5 > 4)


# In[4]:


(5 > 4) or (3 == 5)


# In[6]:


(True and True) and (True == False)


# In[7]:


(not False) or (not True)


# ## Q5. What are the six comparison operators?

# Sol.5:   ==, !=, <, >, <=, and >=

# ## Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# Sol.6: == is the equal to operator that compares two values and evaluates to a 
# Boolean, while = is the assignment operator that stores a value in a variable.

# ## Q7. Identify the three blocks in this code:
# #### spam = 0
# #### if spam== 10
# #### print('eggs')
# #### if spam > 5:
# #### print('bacon')
# #### else:
# #### print('ham')
# #### print('spam')
# #### print('spam')
# 

# Sol.7: The three blocks are everything inside the if statement and the lines 
# print('bacon') and print('ham').

# In[21]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
print('spam')


# ## Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[24]:


#Sol.8: The code:
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


# ## Q9.If your programme is stuck in an endless loop, what keys you’ll press?

# Sol.9:  Press ctrl-c to stop a program stuck in an infinite loop.

# ## Q10. How can you tell the difference between break and continue?

# Sol.10: The break statement will move the execution outside and just after a 
# loop. The continue statement will move the execution to the start of 
# the loop.

# ## Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# Sol.11: They all do the same thing. The range(10) call ranges from 0 up to (but 
# not including) 10, range(0, 10) explicitly tells the loop to start at 0, and 
# range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on 
# each iteration.

# In[29]:


range(10)


# In[31]:


range(0,10)


# In[32]:


range(0,10,1)


# ## Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[34]:


for i in range(1,10):
    print(i)


# In[36]:


i = 1
while i <= 10:
    print(i)
    i = i + 1


# ## Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# Sol.13:  This function can be called with spam.bacon()

# In[ ]:




