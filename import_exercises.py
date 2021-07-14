#!/usr/bin/env python
# coding: utf-8

# # Import Exercises


from function_exercises import calculate_tip

tip = calculate_tip(0.2, 100)

print("Tip amount using imported function: $", tip)


# In[30]:


from function_exercises import get_letter_grade as grade


# In[31]:


grade(98)


# ### How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[47]:


from itertools import product


# In[48]:


print(list(product("abc", [1,2,3])))

len(list(product("abc", [1,2,3])))


# ### How many different combinations are there of 2 letters from "abcd"?

# In[34]:


from itertools import combinations


# In[35]:


len(list(combinations('abcd',2)))


# ### How many different permutations are there of 2 letters from "abcd"?

# In[36]:


from itertools import permutations


# In[37]:


len(list(permutations('abcd',2)))


# # Exercise 3

# In[38]:


import json


# In[3]:


json.load(open('profiles.json'))


# ### Total number of users

# In[4]:


profiles = json.load(open('profiles.json'))


# In[5]:


tot_num_users = len(profiles)
print(tot_num_users)


# ### Number of active users

# In[51]:


active_users = 0
for profile in profiles:
    if profile['isActive'] == True:
        active_users += 1
print(active_users)


# ### Number of inactive users
# 
# 

# In[7]:


inactive_users = 0
for profile in profiles:
    if profile["isActive"] == False:
        inactive_users += 1
print(inactive_users)


# ### Grand total of balances for all users
# 

# In[53]:


total_balance = 0

for profile in profiles:
    balance = profile["balance"]
    balance = balance.replace('$','')
    balance = balance.replace(',','')
    balance = float(balance)
    total_balance += balance
    
print("$",total_balance)


# ### Average balance per user

# In[28]:


avg_bal_per_user = total_balance / tot_num_users

currency = "${:,.2f}".format(avg_bal_per_user)
    
print(currency )


# ### User with the lowest balance

# In[10]:




for profile in profiles:
        
    low = min(profiles, key=lambda profile: profile["balance"]) 
        
print(low["balance"])


# ### User with the highest balance

# In[11]:


for profile in profiles:
        
    high = max(profiles, key=lambda profile: profile["balance"])  
        
print(high["balance"])


# ### Most common favorite fruit
# 

# In[12]:


from collections import Counter

c = Counter()

for profile in profiles:  
    
    c[profile["favoriteFruit"]] += 1
    
print(c)

print("\nMost common favorite fruit is: ", max(c))
 


# ### Least most common favorite fruit

# In[13]:


from collections import Counter

c = Counter()

for profile in profiles:  
    
    c[profile["favoriteFruit"]] += 1
    
print(c)

print("\nLeast common favorite fruit is: ", min(c))


# ### Total number of unread messages for all users

# In[56]:


l = []
sum = 0

for profile in profiles:  

    g = profile["greeting"]
    print(g)
    
    i = 0
    while g[i].isalpha() == True:
            l = ''.join([i for i in g if i.isnumeric()])
            sum = sum + int(l)
            i += 1
            
            #print(l, sum)
        
            break
    
print("\nTotal number of unread messages for all users is: ", sum)


# In[ ]:




