from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC5dcbbfa9eb02f0e23b7d9111c3e3ea24"
# Your Auth Token from twilio.com/console
auth_token  = "d3e68d216150659f6fb7af094fbecfca"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917906843288", 
    from_=" +12028301496",
    body="Hello !")

print(message.sid)
