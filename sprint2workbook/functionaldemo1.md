# Functional demo loop

```python

# Note: text messages 1-5 are for illustrative purposes only, and the data elicited from them would in reality be drawn from the database

# Note: consider where to go the website

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
optimal_pt_bonus = 50
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

# Machine: text message 10

term_end_date = "30 October 2016"

if message9 == 1:
  deposit_amount = optimal_deposit
  point_change = optimal_pt_bonus
  "Awesome! We are transferring $%r and will let you know when it's gone through!" % (optimal_deposit)
elif message9 == 2:
  "That's cool, don't forget that you need to contribute at least $%r by %r to keep your buddies in the black! And don't forget that the sooner you deposit your funds, the more money.days you'll earn!" % (minimum_minimum_deposit, term_end_date)
elif message9 == 3:
  "Awesome, how much do you want to deposit?"
else:
  "ERROR, CANNOT COMPUTE! (Jokes! Please message me 1, 2 or 3, and I'll sort you out)" # probably should be on the look out for other prompts here, or at least throw to the website

# User: text message 10A

# Find a way to note that we only wait for this text if option 3 was chosen

message10A = "250"

# Machine: text message 10B

deposit_amount = message10A
superoptimal_point_bonus = 50

if deposit_amount > optimal_deposit:
  point_change = optimal_pt_bonus + superoptimal_point_bonus
  "What a champion! Have 50 money.days on the house! We are transferring $%r and will let you know when it's gone through!" % (deposit_amount)
elif deposit_amount + savings_excess >= minimum_deposit:
  "Cool beans! We are transferring $deposit_amount and will let you know when it's gone through!"
else:
  "Great! Don't forget that your group is counting on you to contribute %r by %r. We are transferring $%r and will let you know when it's gone through!" % (minimum_minimum_deposit, end_date, deposit_amount)

# Machine: text message 11

savings_balance = 1200
goal_achievement_ratio = (savings_balance / goal_amount * 100)

"You've saved $%r: %r of the way to that %r you wanted." % (savings_balance, goal_achievement_ratio, goal_name)

# Machine: text message 12

point_balance = 260
jackpot_amount = 80
bigmac_cost = 3
bigmac_number = jackpot_amount / bigmac_cost

"You have %r money.days and have about the same chance of winning the jackpot as a grown-up ordering a big-mac when he goes to Micky Dees! Incidentally, you could buy %r Big Macs with that Jackpot, but don't!}" % (point_balance, bigmac_number)
