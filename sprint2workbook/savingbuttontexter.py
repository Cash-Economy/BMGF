# Mario savings button texterer

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "XXXXXXXXXXX1"
AUTH_TOKEN = "XXXXXXXXXXX2"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+16179521274",
    from_="+16072755081",
    body="Congratulations! You have made a deposit.",
)
