# functionaldemo.py
# attempt 1

# Note: text messages 1-5 are for illustrative purposes only, and the data elicited from them would in reality be drawn from the database
# Note: consider when to link to site

## init
from flask import Flask, request, redirect
from twilio import twiml
from datetime import datetime, timedelta

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

messagecount = int(request.cookies.get('messagecount',0))
messagecount += 1

resp = make_response(str(twml))

expires=datetime.utcnow() + timedelta(hours=4)
resp.set_cookie('messagecount',value=str(messagecount),expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))

## Message 1 (response)

if messagecount == 0:
    def incoming_sms():
        body = request.values.get('Body', None)

        g_name = body

        resp=twiml.Response()

        resp.message("Hi %r! Welcome to money.days. I'm going to help you save with your friends, dynamically! But first, what's your family name?" % (g_name))

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)

## Message 2 (response)
elif messagecount == 1:
    def incoming_sms():
        body = request.values.get('Body', None)

        f_name = body

        resp=twiml.Response()

        resp.message("So, the name's %r, %r %r. From what I've heard about savings, a person is much more likely to be successful in their savings if they are saving *for* something. What are you saving up for?" % (f_name, g_name f_name))

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)

## Message 3 (repsonse)
elif messagecount == 2:
    def incoming_sms():
        body = request.values.get('Body', None)

        goal_name = body

        goal_amount = 5000

        income_amount = 1500

        minimum_deposit = 200
        optimal_deposit = minimum_deposit*1.1
        optimal_pt_bonus = 50
        savings_excess = 150
        minimum_minimum_deposit = minimum_deposit - savings_excess

        resp.message("So, you're saving $%r, for %r! That's pretty funky, I'd like to save up for something like that!" % (goal_amount, goal_name))

## Message 4 (continuation, therefore within the same "response" protocol as the above)

        resp.message("It looks like you've received a deposit of $%r!" % (income_amount))

## Message 5 (continuation, therefore within the same "response" protocol as the above)

        resp.message("""
        If you deposit %r you'll be well on the way to getting that new %r you wanted! Do you want to make that deposit?
        1 : Yes, I want to add %r and %r points to my balance
        2 : No, I'll contribute the %r before the end of the month
        3 : I want to contribute a different amount
        """ % (optimal_deposit, goal_name, optimal_deposit, optimal_deposit_pt_bonus, minimum_minimum_deposit))

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)

# Message 6 (response)
elif messagecount == 3:
    def incoming_sms():
        body = request.values.get('Body', None)

        mesage9 = body
        term_end_date = "30 October 2016"

        resp=twiml.Response()

        if message9 == 1:
            deposit_amount = optimal_deposit
            point_change = optimal_pt_bonus
            resp.message("Awesome! We are transferring $%r and will let you know when it's gone through!" % (optimal_deposit))
        elif message9 == 2:
            resp.message("That's cool, don't forget that you need to contribute at least $%r by %r to keep your buddies in the black! And don't forget that the sooner you deposit your funds, the more money.days you'll earn!" % (minimum_minimum_deposit, term_end_date))
        elif message9 == 3:
            resp.message("Awesome, how much do you want to deposit?")
        else:
            resp.message("ERROR, CANNOT COMPUTE! (Jokes! Please message me 1, 2 or 3, and I'll sort you out)") # probably should be on the look out for other prompts here, or at least throw to the website

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)

# Message 7 (Response, only triggered on message9 == 3)
elif messagecount == 4 and message9 == 3:
    def incoming_sms():
        body = request.values.get('Body', None)

        message10A = body
        superoptimal_point_bonus = 50

        resp=twiml.Response()

        if deposit_amount > optimal_deposit:
            point_change = optimal_pt_bonus + superoptimal_point_bonus
            resp.message("What a champion! Have 50 money.days on the house! We are transferring $%r and will let you know when it's gone through!" % (deposit_amount))
        elif deposit_amount + savings_excess >= minimum_deposit:
            resp.message("Cool beans! We are transferring $deposit_amount and will let you know when it's gone through!")
        else:
            resp.message("Great! Don't forget that your group is counting on you to contribute %r by %r. We are transferring $%r and will let you know when it's gone through!" % (minimum_minimum_deposit, end_date, deposit_amount))

    if __name__ == "__main__":
        app.run(debug=True)

# Message 8, 9 (continuation of Mesasage 6, or 7 if message9 == 3)
elif messagecount == 5 and message9 == 3:
        def incoming_sms():
            body = request.values.get('Body', None)

        savings_balance = 1200
        goal_achievement_ratio = (savings_balance / goal_amount * 100)
        point_balance = 260
        jackpot_amount = 80
        bigmac_cost = 3
        bigmac_number = jackpot_amount / bigmac_cost

        resp=twiml.Response()

        resp.message("You've saved $%r: %r of the way to that %r you wanted." % (savings_balance, goal_achievement_ratio, goal_name))

        resp.message("You have %r money.days and have about the same chance of winning the jackpot as a grown-up ordering a big-mac when he goes to Micky Dees! Incidentally, you could buy %r Big Macs with that Jackpot, but don't!" % (point_balance, bigmac_number))

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)

# alt

elif messagecount == 4 and message9 != 3:
        def incoming_sms():
            body = request.values.get('Body', None)

        savings_balance = 1200
        goal_achievement_ratio = (savings_balance / goal_amount * 100)
        point_balance = 260
        jackpot_amount = 80
        bigmac_cost = 3
        bigmac_number = jackpot_amount / bigmac_cost

        resp=twiml.Response()

        resp.message("You've saved $%r: %r of the way to that %r you wanted." % (savings_balance, goal_achievement_ratio, goal_name))

        resp.message("You have %r money.days and have about the same chance of winning the jackpot as a grown-up ordering a big-mac when he goes to Micky Dees! Incidentally, you could buy %r Big Macs with that Jackpot, but don't!" % (point_balance, bigmac_number))

        return str(resp)

    if __name__ == "__main__":
        app.run(debug=True)
