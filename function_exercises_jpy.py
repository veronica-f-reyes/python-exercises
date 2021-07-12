#!/usr/bin/env python
# coding: utf-8

# # 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[35]:


def is_two(a):
    if (a == str(2) or a == int(2)):
        print(a, type(a))
        return True
    else:       
        return False


# # 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

# In[29]:


def is_vowel(a):
    if (a in "AEIOUaeiou"):
        return True
    else:
        return False


# # 3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this. 

# In[37]:


def is_consonant(c):
    if (is_vowel(c) == False):
        return True
    else:
        return False


# In[39]:


is_consonant('b')


# # 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

# In[65]:


def is_word(w):
    if type(w) == str:
        if is_consonant(w[0]):
            print(w.capitalize())
            return w.capitalize()
        else:
            return w
    else:
        print("Input is not a string.")
   


# In[66]:


is_word(1)


# # 5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[56]:


def calculate_tip(pct, bill):
    if (pct < 0 or pct > 1):
        print("Tip percentage must be between 0 and 1")
        return
    else:
        tip_amt = bill * pct
    return tip_amt
    


# In[59]:


calculate_tip(0.5, 100)


# # 6. Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[69]:


def apply_discount(orig, disc):
    price_after_disc = orig - (orig * (disc * 0.01))
    
    if price_after_disc < 0:
        print ("Discount not applied.")
    else:     
        return price_after_disc


# In[73]:


apply_discount(100,25)


# # 7.Define a function named handle_commas.
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[80]:


def handle_commas(num):
    
    num = int(num.replace(',',''))
    
    return num


# In[81]:


handle_commas('2,753,543')


# # 8.Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F). 

# In[104]:


def get_letter_grade(num):
    if (num >= 90 and num <=100):
        return "A"
    elif (num >= 80 and num <=89):
        return "B"
    elif (num >= 70 and num <=79):
        return "C"
    elif (num >= 60 and num <=69):
        return "D"
    elif (num >= 0 and num <=59):
        return "F"
    else:
        print ("Not a valid input to convert to a letter grade.")
        return
    


# In[107]:


get_letter_grade(234564)


# # 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[108]:


def remove_vowels(w):
    vowels = 'AEIOUaeiou'
    w_no_vowels = [letter for letter in w if letter.lower() not in vowels]
    w_no_vowels = ''.join(w_no_vowels)
    
    return w_no_vowels


# In[111]:


remove_vowels('codeup')


# # 10. Define a function named normalize_name.
# It should accept a string and return a valid python identifier, that is:
#    - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#         - Name will become name
#         - First Name will become first_name
#         - % Completed will become completed

# In[ ]:


def normalize_name(name):
    

