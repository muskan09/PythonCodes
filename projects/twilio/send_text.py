

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa9cf9149f34da72a37eb2cefdba2d8ab"
# Your Auth Token from twilio.com/console
auth_token  = "72213c6d70de8ff95144a4edf6d6aacc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919876345548", 
    from_="+912162329541",
    body="MK<3")

print(message.sid)
