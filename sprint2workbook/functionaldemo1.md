# Functional demo loop

```python

# Note: text messages 1-5 are for illustrative purposes only, and the data elicited from them would in reality be drawn from the database

# User: text message 1 - initiates conversation in response to our prompt
message1 = "JoJo" # e.g. of message content

g_name = message1 # Note - this is the first field in a new database entry |||INCORPORATE LATER|||

# Machine: text message 2
"Hi %r! Welcome to money.days. I'm going to help you save with your friends, dynamically! But first, what's your family name?" % (g_name)

# User: text message 3
message3 = "Ottensooser" # e.g. of message content

f_name = message3

# Machine: text message 4
"So, the name's %r, %r %r. From what I've heard about savings, a person is much more likely to be successful in their savings if they are saving *for* something. What are you saving up for?" % (f_name, g_name f_name)

# User: text message 5
message5 = "A trip to Cancun" # e.g. of message content

goal_name = message5

# Machine: text message 6

goal_amount = 5000 # this is a stub, and would actually be called from the database

"A $%r %r! That's pretty funky, I'd like to save up for something like that!" % (goal_amount, goal_name)

# Machine: text message 7

income_amount = 1500

"It looks like you've received a deposit of $%r!" % (income_amount)

# Machine: text message 8

minimum_deposit = 200
optimal_deposit = minimum_deposit*1.1
optimal_deposit_pt_bonus = 50
savings_excess = 150
minimum_minimum_deposit = minimum_deposit - savings_excess

"""
If you deposit %r you'll be well on the way to getting that new %r you wanted! Do you want to make that deposit?
1 : Yes, I want to add %r and %r points to my balance
2 : No, I'll contribute the %r before the end of the month
3 : I want to contribute a different amount
""" % (optimal_deposit, goal_name, optimal_deposit, optimal_deposit_pt_bonus, minimum_minimum_deposit)

# User: text message 9

message9 = "1" # can be 1, 2, or 3

# Machine:
