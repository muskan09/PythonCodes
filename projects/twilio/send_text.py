

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = " add "
# Your Auth Token from twilio.com/console
auth_token  = "add"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="my phone num", 
    from_="twillio phone num",
    body="MK<3")

print(message.sid)
