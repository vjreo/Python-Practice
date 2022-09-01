#!/usr/bin/env python
# coding: utf-8

# In[6]:


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + ' is going to buy the meal today.')


# In[7]:


# using random.choice
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

person_who_will_pay = random.choice(names)
print(person_who_will_pay + ' is going to buy the meal today.')


# In[ ]:




