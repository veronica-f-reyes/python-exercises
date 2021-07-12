#You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
#  and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

lil_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
price_per_day = 3
total_rental_price = (lil_mermaid_days + brother_bear_days + hercules_days) * price_per_day
print(total_rental_price)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.
#They pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
# and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_pay_rate = 400
amazon_pay_rate = 380
facebook_pay_rate = 350

google_hrs_worked = 6
amazon_hrs_worked = 4
fb_hrs_worked = 10

total_pay_for_hrs_worked = (google_pay_rate* google_hrs_worked)+(amazon_pay_rate*amazon_hrs_worked)+(facebook_pay_rate*fb_hrs_worked)
print(total_pay_for_hrs_worked)

print("Total pay is $",total_pay_for_hrs_worked)

contractor_jobs = {
    "company" : 'Google',
    "pay_rate" : 400, 
    "hrs_worked" : 6
}
print(contractor_jobs)

contractor_jobs = [
    contractor_jobs,
    {
        "company" : 'Amazon',
        "pay_rate" : 380, 
        "hrs_worked" : 4
    }
]
print(contractor_jobs)

contractor_jobs = [
    contractor_jobs,
    {
        "company" : 'Facebook',
        "pay_rate" : 350, 
        "hrs_worked" : 10
    }
]
print(contractor_jobs)
print(type(contractor_jobs), type(contractor_jobs))

#for contractor_job in contractor_jobs:
 #  total_pay_for_hrs_worked += (contractor_job["pay_rate"]* contractor_job["hrs_worked"])

total = 0 
#print(contractor_jobs["pay_rate"])
#print(contractor_jobs["hrs_worked"])

for job in contractor_jobs:
 # print(contractor_jobs["pay_rate"])
  print(type(contractor_jobs))
  print(contractor_jobs)
  #pay = contractor_jobs["pay_rate"] * contractor_jobs["hrs_worked"]
#total += pay

print('Total pay is $', total)  
#print(f"Total compensation is ${total}")

#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

can_student_enroll = True
class_is_full = False
class_conflicts = False

if class_is_full or class_conflicts == False:
  print("Student cannot enroll")
else:
  print("Student can enrroll")

can_student_enroll = not(class_is_full) and not(class_conflicts)              
                  
print("Can student enroll? ", can_student_enroll)

#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

is_premium_mbr = False
is_offer_expired = True
more_than_two_items= True

if is_premium_mbr and is_offer_expired:
  print("Product offer applied")
elif more_than_two_items and not is_offer_expired:
  print("Product offer applied")
elif not(more_than_two_items) or is_offer_expired:
    print("Offer is not available")  

offer_can_be_applied = is_offer_expired and (more_than_two_items or is_premium_mbr)

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following conditions:

#The password must be at least 5 characters
is_min_five_chars = True if len(password) >=5 else False
print(is_min_five_chars)

#The username must be no more than 20 characters
is_max_twenty_chars = True if len(username) <=20 else False
print(is_max_twenty_chars)

#the password must not be the same as the username
same_username_pw = True if username == password else False
print(same_username_pw)

#bonus neither the username or password can start or end with whitespace
starts_or_ends_with_blanks = True if (username != username.strip() or password != password.strip()) else False
print(starts_or_ends_with_blanks)

