#!/usr/bin/env python
# coding: utf-8

# # Getting started with Python Basics

# ## Variables ~ Objects

# #### If you are from the world of Java, No need to worry about Initialisation/Declaration Types

# In[1]:


my_country = 'india' #String Object

type(my_country) #You guessed it right - type() is a function to get the type of the object


# In[2]:


this_year = 2017 #Numeric Object

type(this_year)


# In[3]:


next_year = '2018' 

type(next_year)


# In[4]:


na_eq = None
type(na_eq)


# #### When Implicit Coercion works!

# In[211]:


one_banana = 10.5
print(type(one_banana))
ten_bananas = 10.5 * 10
ten_bananas


# #### (Hence) Python interpreter is considered to be a *powerful* calculator

# In[91]:


9 ** 11


# In[92]:


5.6 / 2.3


# In[93]:


120 / 5.4


# In[94]:


22 / 7


# #### When Implicit Coercion fails!

# In[44]:


this_year + next_year


# In[45]:


this_year + int(next_year)


# In[46]:


print('This year is ' + this_year + ' and Next year is ' + next_year)


# In[213]:


print('This year is %d Next year is %s' %(this_year, next_year))


# ### When Indentation hits hard, Welcome to Python!

# In[216]:


print('I know Python is simple and easy ')
print("I know I can use double quotes or single quotes to print") 
print('Perhaps I should Python is Indentation-specific')


# ![img](C:/Users/SA31/Pictures/Guido_Indentation.jpg)

# ### Sequence Types 

# ### List

# In[233]:


numbers = [1,2,3,4,5,6]
type(numbers)


# In[227]:


new_list = list()

new_list


# In[228]:


new_list.append('Jay')
new_list


# #### Python's list is ZERO-indexed (like many other programming languages but unlike R)

# In[98]:


numbers[0]


# In[103]:


numbers[:3]


# In[102]:


numbers[1:3]


# ### List Iteration

# In[231]:


len(numbers)


# #### The hard way

# In[234]:


for i in range(len(numbers)):
    print(numbers[i] * 5)


# #### The easy way

# In[101]:


for number in numbers:
    print(number * 5)


# ### Tuples

# In[117]:


a = (1,2)


# In[119]:


type(a)


# In[142]:


print(numbers)
numbers_tuple = tuple(numbers)
print(numbers_tuple)
print(list(tuple(numbers)))


# In[235]:


[1,2,3,[1,2],[2,4]]


# #### Mutable List vs Immutable Tuple

# In[238]:


['abdul',23]


# In[237]:


name,age = 'abdul',23

print(name)
print(age)


# In[ ]:


#### Appending a new list element using .append() r


# In[241]:


numbers.append(7)

numbers


# In[242]:


numbers[2] = 999

numbers


# In[243]:


numbers_tuple[2] = 1212


# In[250]:


new_numbers = numbers # Does not copy the list

new_numbers[3] = 45454

new_number = numbers[:]


# In[251]:


numbers[4] = 444666566

print("This is numbers, the original", numbers)

print("This is new_numbers which was created from numbers", new_numbers)


# In[156]:


colors = ['red', 'blue', 'green']
b = colors 


# ![list](https://developers.google.com/edu/python/images/list2.png)

# In[253]:


dir(tuple)


# #### A little List manipulation

# #### with the method *.sort()*

# In[255]:


from random import randint,seed
seed(124)
empty_list = []
for n in range(23):
    empty_list.append(randint(0, 9))
    

print('Before Sorting........................\n')    
print(empty_list)
print('\nAfter Sorting.........................\n')
empty_list.sort()
print(empty_list)


# #### with the built-in function *sorted()*

# In[181]:


from random import randint,seed
seed(123)
empty_list = []
for n in range(23):
    empty_list.append(randint(0, 9))
    

print('Before Sorting........................\n')    
print(empty_list)
print('\nAfter Sorting.........................\n')
sorted_empty_list = sorted(empty_list)
print(sorted_empty_list)


# ### String Manipulation

# In[61]:


til = 'Pseudonymization'


# #### Length of the string

# In[62]:


len(til)


# #### String Concatenation

# In[75]:


til + ' is not Anonymization '


# #### String Repetition 

# In[267]:


til + '5' 


# In[265]:


(til + ' is not Anonymization ') * 5


# ### Strings are immutable sequence types (~ remember *List*?)

# In[77]:


til[:]


# #### Hence substring is just *list slicing*

# In[82]:


til[0]


# In[80]:


til[:6]


# In[84]:


til[5:]


# In[271]:


til[:-1]


# #### But immutable!

# In[272]:


til[0] = 'p'


# In[274]:


pi = 3.14
#text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes
text


# #### String Split

# In[277]:


fruits = 'Apple Orange Pomo Melon Berry'
fruits


# In[281]:


fruits_list = fruits.split()


# In[283]:


"|".join(fruits_list)


# ### Dictionary

# In[1]:


details = {'a':'abc@gmail.com','b':'bcd@gmail.com','c':'cbd@gmail.com'}
type(details)


# In[2]:


empty_dict = {}

empty_dict['india'] = 'new delhi'

empty_dict.keys()


# In[4]:


for key in details:
    print(key)


# In[3]:


details[4] = [1,2,3,4]

details


# ### Conditional Loops

# In[5]:


for key in details:
    if key == 'a':
        print(key + ' rocks!!!')


# In[300]:


if 0:
    print('Wow high school math is right!')
else:
    print('Oops')


# #### User-defined Functions

# In[314]:


def welcome(name):
    print('helo')
    print('welcome to india')
    print('Welcome to Python, '+name)


# In[315]:


welcome('Siddesh')


# #### Function with List comprehension - Pythonic

# In[309]:


def multiplication_table(number):
    print([i * number for i in range(1,10)])


# In[308]:


[i*3 for i in range(1,10)]


# In[305]:


for i in range(1,10):
    print(i * 3)


# In[ ]:





# In[310]:


multiplication_table(2)


# In[196]:


multiplication_table(3)


# ### Finally, All Hail Modules! 
# 
# ![img](C:\Users\SA31\Pictures\python.png)

# In[316]:


import antigravity


# In[ ]:


from matplotlib import pyplot


# In[317]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(numbers)


# ### Reading List:
# 
# * [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
# * [AutomatetheBoringStuff with Python - Chapter 1](https://automatetheboringstuff.com/chapter1/)
# 
