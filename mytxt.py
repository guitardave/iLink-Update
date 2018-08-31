#mytxt.py

from twilio.rest import Client
acct = "AC94af148f4f4bb3de920e2211b8daf6d4"
auth = "c6ef06c790e2e045bd9ff28d1a11d036"
twilioc = Client(acct, auth)
myNumber = "+18174096768"
myCell = "+14695855009"
msg = twilioc.messages.create(body="Kisses Mama! This is an app I wrote to send txt messages through a 3rd party interface. Loves Mama!", from_=myNumber, to=myCell)
print "Message Sent"