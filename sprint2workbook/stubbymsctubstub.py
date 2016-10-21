from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = twiml.Response()

    # Determine the right reply for this message
    if len(body) >= 3:
        resp.message("""
        Hi %r! Welcome to money.days. Let's save! Looks like theres a deposit of $1500 in your account, this is more than your usual income, awesome! What do you want to do?
        1: I want to deposit $400, because I earned a little more, and earn 50 bonus money.days!
        2: I want to deposit $300, as usual!
        3: I don't want to make a deposit.
        4: I want to make a custom deposit.
        """) % (body)
    elif body == '1':
        resp.message("Champion! Saving more when you earn more helps you when you earn less. We've made the deposit and will let you know when it goes through.")
    elif body == "2":
        resp.message("Great! Regular savings are good savings!")
    elif body == "3":
        resp.message("That's cool, but don't forget that you need to contribute at least $400 by next Thursday to keep your buddies in the black! And don't forget that the sooner you deposit your funds, the more money.days you'll earn!?")
    elif body == "4":
        resp.message("""
        Awesome, how much do you want to save?
        A: 100
        B: 200
        C: 500
        """)
    elif body == "A":
        resp.message("Awesome $100 deposited. Don't forget that you'll need to contribute another $300 by next Thursday to keep your buddies in the black.")
    elif body == "B":
        resp.message("Awesome $200 deposited. Don't forget that you'll need to contribute another $200 by next Thursday to keep your buddies in the black.")
    elif body == "C":
        resp.message("*claps* $500 deposited. You've blown me away. Here, take 200 bonus money.days. This has increased your chance of winning the jackpot to about the same chance as a grown-up ordering a big-mac when at Micky-Dees! Coincidentally, you could buy 35 big-macs with the jackpot, but don't!")
    else:
        resp.message("ERROR, DOES NOT COMPUTE! (Jokes! Please message me 1, 2 or 3, and I'll sort you out)") # probably should be on the look out for other prompts here, or at least throw to the website

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
