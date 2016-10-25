#use http://kj-twilio.herokuapp.com/sms

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
    if body == '1':
        resp.message("Awesome! We are transferring $2000 and will let you know when it's gone through!")
    elif body == '2':
        resp.message("That's cool, don't forget that you need to contribute at least $400 by Thursday to keep your buddies in the black! And don't forget that the sooner you deposit your funds, the more money.days you'll earn!")
    elif body == "3":
        resp.message("Awesome, how much do you want to deposit?")
    else:
        resp.message("ERROR, CANNOT COMPUTE! (Jokes! Please message me 1, 2 or 3, and I'll sort you out)") # probably should be on the look out for other prompts here, or at least throw to the website


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
