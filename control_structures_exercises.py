#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
prompt_for_day = input("What day of the week is it? ")
print(prompt_for_day)

if prompt_for_day.lower() == "monday":
    print("Yup, today is Monday.")
else:
    print("Today is not Monday.  It is ", prompt_for_day)


# In[5]:


#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
prompt_for_day = input("What day of the week is it? ")
print(prompt_for_day)

if prompt_for_day.lower() in ("saturday", "sunday"):
    print("Woohoo! It is the weekend!!")
else:
    print("Not the weekend.  Boo..")


# #create variables and make up values for:
# #the number of hours worked in one week
# #the hourly rate
# #how much the week's paycheck will be
# #write the python code that calculates the weekly paycheck. 
# #You get paid time and a half if you work more than 40 hours

# In[12]:


hrs_worked_per_week = 41
hourly_rate = 100
 
if hrs_worked_per_week <= 40:
    weekly_paycheck = hrs_worked_per_week * hourly_rate
else:
    overtime = (hrs_worked_per_week - 40) * (hourly_rate * 1.5)
    weekly_paycheck = (40 * hourly_rate) + overtime
        
print("Weekly paycheck: $", weekly_paycheck)


# # Loop Basics - While

# In[13]:


#Create an integer variable i with a value of 5.

i = 5

#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

while i <= 15:
    print(i)
    i += 1


# In[14]:


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0

while i <=100:
    print(i)
    i += 2


# In[15]:


#Alter your loop to count backwards by 5's from 100 to -10.
i = 100

while i >= -10:
    print(i)
    i -= 5


# In[17]:


#Create a while loop that starts at 2, and displays the number squared on each line
#while the number is less than 1,000,000. 

i = 2

while i < 1000000:
    print(i)
    i = (i*i)    


# In[18]:


#Write a loop that uses print to create the output shown below.
i = 100

while i >= 5:
    print(i)
    i -= 5


# # For Loops
# 
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[27]:


user_number = input("Which number would you like to try? ")
i = 0
while i <= 10:
    mult = int(user_number) * int(i)
    print(user_number, " x ", i, " = ", mult)
    i += 1
    


# In[47]:


#Create a for loop that uses print to create the output shown below.
for n in range(10):
    print(str(n) * n )


# # break and continue
# 
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[148]:


prompt_for_odd_number = input("Give me an odd number between 1 and 50, please.  --> ")

while prompt_for_odd_number.isdigit() == False or int(prompt_for_odd_number) > 50:
    print("Input is not an valid value.")
    prompt_for_odd_number = input("Give me an odd number between 1 and 50, please.  --> ")
    continue

while prompt_for_odd_number.isdigit() and int(prompt_for_odd_number) < 50:
    
    if (int(prompt_for_odd_number) % 2) == 0: 
        print("Input is not an valid value.  You entered an even number.")
        prompt_for_odd_number = input("Give me an odd number between 1 and 50, please.  --> ")
        continue
    print("Number to skip is ", prompt_for_odd_number)   
        
    for i in range(50):
        
        if int(i) == int(prompt_for_odd_number):
            print(f'Yikes! Skipping number: {prompt_for_odd_number}')
            continue
        if i % 2 == 0:
            continue
        print(f'Here is an odd number: {i}')     
         
    i = i+1
 
    break

    
    


# # D.
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[147]:


prompt_for_positive_number = input("Let's think positive! Enter a positive number, please.  --> ")

while prompt_for_positive_number.isdigit() == False or int(prompt_for_positive_number) < 0 :
    print("D'oh! That's not positive or a number.")
    prompt_for_positive_number = input("Let's think positive! Enter a positive number, please.  --> ")
    continue
    
while prompt_for_positive_number.isdigit() and int(prompt_for_positive_number) > 0:
  
    print(f'Ok, let\'s count to : {prompt_for_positive_number}')
    
    for i in range(int(prompt_for_positive_number)+1):
        
        print(i)     
         
    i = i+1
 
    break    


# # E.
# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[125]:


prompt_for_positive_number = input("Let's think positive! Enter a positive number, please.  --> ")

while prompt_for_positive_number.isdigit() == False or int(prompt_for_positive_number) <= 0 :
    print("D'oh! That's not positive or a number.")
    prompt_for_positive_number = input("Let's think positive! Enter a positive number, please.  --> ")
    continue
    
while prompt_for_positive_number.isdigit() and int(prompt_for_positive_number) > 0:

    i = int(prompt_for_positive_number)   
    print(f'Ok, let\'s count backwards from : {prompt_for_positive_number}')
    
    while i >= 1 :
        print(i)
        i -= 1
 
    break    


# # 3. Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# In[155]:


print(f'Fizz, buzz, FizzBuzz!  Ok, let\'s count to 100! \n')  

for i in range(1,100+1):
    
    if (int(i) % 3) == 0 and not((int(i) % 5) == 0): 
        print("Fizz")    
     
    elif (int(i) % 5) == 0 and not((int(i) % 3) == 0) : 
        print("Buzz")       
        
    elif (int(i) % 5) == 0 and ((int(i) % 3) == 0) : 
        print("FizzBuzz")      
    else:
        print(i)  
         

 
 


# # 4. Display a table of powers.
# 
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# In[214]:


# import module
#from tabulate import tabulate

want_to_continue = True

while want_to_continue == True:
    n = input("What number would you like to go up to? Enter an integer.  --> ")
    n = int(n)

    print("\n Here is your table!\n")
    
    print('number | squared | cubed')
    print('------ | ------- | -----')
    
    for n in range(1, n+1, 1):
        print(f'{n:<7}| {n**2:<8}| {n**3}')

#Same output not formatted to compare

    for i in range(1,n+1):
    
        mydata = [i, i*i, i**3]
        print(mydata)
    
    want_to_continue = input("\nDo you want to try another number? ")
    if want_to_continue == "no" or want_to_continue == "n":
        print("\nOk, have a nice day!")
        break
    else:
        print('\nGreat! Let\'s try another!')
        want_to_continue = True
       
 
       
 



# # 5. Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# In[208]:


want_to_continue = True

while want_to_continue == True:
    n = input("Please enter a grade value between 0 - 100.  --> ")
    n = int(n)

    if n >= 99 and n <=100:
        print("\nThe letter grade for the value entered is:  A+")  
    elif n >= 88 and n <=98:
        print("\nThe letter grade for the value entered is:  A")     
    elif n >= 80 and n <=87: 
        print("\nThe letter grade for the value entered is:  B")
    elif n >= 67 and n <=79: 
        print("\nThe letter grade for the value entered is:  C")   
    elif n >= 60 and n <=66: 
        print("\nThe letter grade for the value entered is:  D") 
    elif n >= 0 and n <=59: 
        print("\nThe letter grade for the value entered is:  F")
    else:
        print("Entered value not valid. Try entering a valid number between 0 - 100. ")
    
    want_to_continue = input("\nDo you want to enter another grade value? ")
    
    if want_to_continue == "no" or want_to_continue == "n":
        print("\nOk, have a nice day!")
        break
    else:
        print('\nGreat! Let\'s try another!\n')
        want_to_continue = True


# # 6. Create a list of dictionaries 
# 
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# 

# In[223]:



books = [
    {
        "title": "Introduction to Applied Linear Algebra",
        "author": "John Smith",
        "genre": "Non-fiction"
    },
    
    {
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "genre": "Fantasy"
    },
    
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Youth"
    },
    
    {
        "title": "FitGurl",
        "author": "Mel Alcantara",
        "genre": "Self-Help"
    },
]

for book in books:
    print("Title: ", book["title"],"\nAuthor: ",  book["author"],"\nGenre: ", book["genre"], "\n")
    


# # 6 a.
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[235]:


prompt_book_genre = input("What book genre would you like to search through? --> ")

books = [
    {
        "title": "Introduction to Applied Linear Algebra",
        "author": "John Smith",
        "genre": "Non-fiction"
    },
    
    {
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "genre": "Fantasy"
    },
    
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Young Adult Fiction"
    },
    
    {
        "title": "FitGurl",
        "author": "Mel Alcantara",
        "genre": "Self-Help"
    },
    
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "genre": "Young Adult Fiction"
    },
    
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen Covey",
        "genre": "Self-Help"
    }
]



for book in books:
    if(prompt_book_genre == book["genre"]):
        print("\nTitle: ", book["title"],"\nAuthor: ",  book["author"],"\nGenre: ", book["genre"], "\n")


# In[ ]:





# In[ ]:




