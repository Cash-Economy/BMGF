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

### wishlist
- different responses for different amount of times that the User chooses option 2, or option 3 where deposit_amount < minimum_deposit (increasingly whiney)
- different end messages
  - funny expressions of lottery odds
  - time to goal where that is motivating (e.g. short term where goal_sum is reasonable)
- if Trns within half a standard deviation of mean_time && Regular_amount being different from edge case inputs
- regular input being different from a windfall

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
    "My Man! How much can you put away today?"
    "${deposit_amount}! Awesome, you are {minimum_deposit - deposit_amount} away from saving up all you need for the {period}! We are transferring ${deposit_amount} and will let you know when it's gone through!"
    "You've saved ${total_savings balance}: {total_savings / goal_amount*100}% of the way to that {goal_name} you wanted."
    "You have {x} money.days and have {about the same chance of winning the jackpot as a person winning a pinewood derby, when there are five other entrants! You could buy {jackpot_amount/7} pinewood derby kits with the jackpot, but don't!}"
  if "2":
    "That's cool - don't forget you've got ${minimum_deposit-excess} to save before the end of the {period}."
```

### wishlist
- different positive and negative net period contribution statements after deposit
- more nuanced successes after deposit

## Unprompted message

On a day without any bank transaction or activity on money.days, to maintain user engagement

```
"""Hola {Name}! Did you know your savings of ${total_savings} have been working hard for you? In the {today - last_message_date} days we last spoke your money.days balance has grown by {total_points - prev_points_balance} giving you a grand total of {total_points} money.days. That increases your chance of winning the jackpot by as much as the chance of walking through three green walking man traffic lights in a row! Do you want to make another deposit today?
1 : Yup, I'm hungry for that jackpot!
2 : Nah, maybe another time.."""
  if "1":
    "Sweet! How much are you saving today?"
    "Sounds good, we're transferring ${deposit_amount} and will hit you up when it's gone through! This takes your new savings balance to ${total_savings} and gets you {total_savings / goal_amount*100}% towards that {goal_name}!"
  if "2":
    "That's alright, have a great day! Talk to you soon!"
```

