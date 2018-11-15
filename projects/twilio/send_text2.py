from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "bleh"
# Your Auth Token from twilio.com/console
auth_token  = "bleh"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to=" v", 
    from_="vjhn",
    body="MK<3")

print(message.sid)
