#!/usr/bin/env python
# coding: utf-8

# # 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[35]:

# This  is_two function defines a single parameter, a, that is either a string or an integer, 
# and will return a boolean if it is either a string or integer of value 2
def is_two(a):
    if (a == str(2) or a == int(2)):
        return True
    else:       
        return False

print (is_two(2))

# # 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

# In[29]:

# This  is_vowel function defines a single parameter, a, that is a string, 
# and will return a boolean of value True if it is vowel
def is_vowel(a):
    if (a in "AEIOUaeiou"):
        return True
    else:
        return False

print(is_vowel('A'))

# # 3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this. 

# In[37]:

# This  is_consonant function defines a single parameter, c, that is a string, 
# and will return a boolean of value True if it is consonant
def is_consonant(c):
    if (is_vowel(c) == False):
        return True
    else:
        return False

print(is_consonant('A'))
# In[39]:


is_consonant('b')


# # 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

# In[65]:

# This is_word function defines a single parameter, w, that is a string, 
# and will return a string where the first letter of the word is capitalized if the word starts with a consonant
def is_word(w):
    if type(w) == str:
        if is_consonant(w[0]):
            print(w.capitalize())
            return w.capitalize()
        else:
            return w
    else:
        print("Input is not a string.")
   
print(is_word('Alpha'))

# In[66]:


is_word(1)


# # 5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[56]:

# This calculate_tip function defines two parameters, pct and bill, that are integers, and
# calculates the tip by multiplying the bill amount and the tip percentage and returning an integer 
def calculate_tip(pct, bill):
    if (pct < 0 or pct > 1):
        print("Tip percentage must be between 0 and 1")
        return
    else:
        tip_amt = bill * pct
    return tip_amt
    

print(calculate_tip(.2,100))
# In[59]:


calculate_tip(0.5, 100)


# # 6. Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[69]:

# This apply_discount function defines two parameters that are integers, and
# calculates the discounted price after taking the percentage discount and using it to calulated the discount price and 
# subtracting it from the original price.  It returns an integer.
def apply_discount(orig, disc):
    price_after_disc = orig - (orig * (disc * 0.01))
    
    if price_after_disc < 0:
        print ("Discount not applied.")
    else:     
        return price_after_disc

print(apply_discount(100,20))
# In[73]:


apply_discount(100,25)


# # 7.Define a function named handle_commas.
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[80]:

# This handle_commas function defines one parameter that is a string and replaces takes out any commas to return an integer.
def handle_commas(num):
    
    num = int(num.replace(',',''))
    
    return num

print(handle_commas('1,234,234'))
# In[81]:


handle_commas('2,753,543')


# # 8.Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F). 

# In[104]:

# This get_letter_grade function defines one parameter that is a number and determines what letter grade it is 
# equivalent to and returns a string.

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
    
print(get_letter_grade(90))

# In[107]:


get_letter_grade(234564)


# # 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[108]:

#This function, remove_vowels, accepts a string and returns a string with all the vowels removed
def remove_vowels(w):
    vowels = 'AEIOUaeiou'
    w_no_vowels = [letter for letter in w if letter.lower() not in vowels]
    w_no_vowels = ''.join(w_no_vowels)
    
    return w_no_vowels

print(remove_vowels('codeup'))
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

#This function, normalize_name, accepts a string and converts it into a valid python identifier with no starting numbers, 
#special characters, or spaces at the beginning and end.  It also remove any special characters within the string.
#It returns a string.
def normalize_name(n):

    n = n.strip()
    n = n.lower()
    n = n.replace(' ', '_')

    # input is already cleaned up after initial processing
    if n.isidentifier() == True:    
        print("It works!")
        return n
    
    # input starts with numbers 
    elif n[0].isnumeric() == True: 
        print("I'm here")
        n= ''.join([i for i in n if (not i.isdigit() and i.isalpha() or i == '_')])
        
        if n == "":
            print("Value cannot be only digits")
            return
        else:
            return n
     
    # input starts with special characters  
    elif n[0].isalpha() == False:
        print("Starts with special chars")
        i = 0
        while n[i].isalpha() == False:
            n= ''.join([i for i in n if (i.isalpha() or i == '_')])
            i = i + 1
            
            return n
        
            break
     
    # input contains special characters 
    else: 
        i = 0
        while n[i].isalpha() == True:
            n= ''.join([i for i in n if (i.isalpha() or i == '_')])
            i = i + 1
            
            return n
        
            break

    

#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]        

#This function, cumulative_sum, accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list       
def cumulative_sum(num):
    
    total = 0
    
    total_sum_list= []
    
    for i in num:
            
            total += i
            
            total_sum_list.append(total)
            
    return total_sum_list  

print(cumulative_sum([1,2,3,4]))
