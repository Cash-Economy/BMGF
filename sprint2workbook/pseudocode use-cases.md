# Pseudocode Use-cases

## Incoming deposit
```
[transaction notification received via Plaid:
  Trns{
    Time
    Deposit of $x}]

"Hi {Name}! It looks like you've received a deposit of ${X}!"
  """If you deposit {minimum_deposit + 10%} you'll be well on the way to getting that new {goal_name} you wanted! Do you want to make this deposit?
  1 : Yes, I want to add {minimum_deposit + 10%} and {points} points to my balance
  2 : No, I'll contribute the {minimum_deposit} before the end of the month
  3 : I want to contribute a different amount"""
  if "1":
    "Awesome! We are transferring ${minimum_deposit + 10%} and will let you know when it's gone through!"
  if "2":
    "That's cool, don't forget that you need to contribute at least ${minimum_deposit - excess} by {end_date} to keep your buddies in the black! And don't forget that the sooner you deposit your funds, the more money.days you'll earn!"
  if "3"
    "Awesome, how much do you want to deposit?"
    if deposit_amount > {minimum_deposit + 10%}:
      "What a champion! Have 50 money.days on the house! We are transferring ${deposit_amount} and will let you know when it's gone through!"
    if {minimum_deposit - excess} > deposit_amount > minimum_deposit:
      "Cool beans! We are transferring ${minimum_deposit + 10%} and will let you know when it's gone through!"
    if deposit_amount < minimum_deposit:
      "Great! Don't forget that your group is counting on you to contribute {minimum_deposit - (excess + deposit_amount)} by {end_date}. We are transferring ${deposit_amount} and will let you know when it's gone through!"
"You've saved ${total_savings balance}: {total_savings / goal_amount*100}% of the way to that {goal_name} you wanted."

"You have {x} money.days and have {about the same chance of winning the jackpot as a grown-up ordering a big-mac when he goes to Micky Dees! Incidentally, you could buy {jackpot_amount/3} Big Macs with that Jackpot, but don't!}"
```

## Friend makes a deposit

On day where User doesn't make a deposit but there is a deposit in the groups

```
"Psst, one of your savings compatriots made a deposit today. Do you want to save a few bucks to get you closer to getting that {goal_name} you wanted? It'll also help you catch some money.days on the competition for the jackpot."

"""
I'll tell you what, between you and me, I'll give you 10 bonus money.days if you put something aside today. What do you say?
1 : For you? Of course!
2 : Nah, thanks though...
"""
  if "1":
    "My Man! "
```

## wishlist
- different responses for different amount of times that the User chooses option 2, or option 3 where deposit_amount < minimum_deposit (increasingly whiney)
- different end messages
  - funny expressions of lottery odds
  - time to goal where that is motivating (e.g. short term where goal_sum is reasonable)
- if Trns within half a standard deviation of mean_time && Regular_amount being different from edge case inputs
- regular input being different from a
