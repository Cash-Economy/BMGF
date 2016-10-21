# Functional demo loop

```python
# User: text message 1 - initiates conversation in response to our prompt
message1 = "JoJo"

g_name = message1

# Machine: text message 2
"Hi %r! Welcome to money.days. I'm going to help you save with your friends, dynamically! But first, what's your family name?" % (g_name)

# User: text message 3
message3 = "Ottensooser"

f_name = message3

# Machine: text message 4
"So, the name's %r, %r %r. From what I've heard about savings, a person is much more likely to be successful in their savings if they are saving *for* something. What are you saving up for?" % (f_name, g_name f_name)

# User: text message 5
message5 = "A trip to Cancun"

goal_name = message5

# Machine: text message 6

goal_amount = 5000

"A $%r %r! That's pretty funky, I'd like to save up for something like that!" % (goal_amount, goal_name)
