# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
msg = input("Please type your message here...")

#Nikhil's Credentials
#account_sid = "ACe996d6fda1a47cadf642fe4cc3a929e2"
#auth_token = "dd1a9f4ccbf9765b861009c6d36f0ec6"

#Sunil's Credentials
account_sid = "ACd0b71e07b00a3c7592ffd9a74460164b"
auth_token = "6117c87ddb188b117f00f10aaa3928a3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    "+918123813253",
    body= msg,
    from_="+15162267464",
   # media_url="http://www.example.com/cheeseburger.png"
)

print(message.sid)

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Issues:

# Same as previous projects
# Follow guidelines as specified

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
