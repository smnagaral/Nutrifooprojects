# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import os


def setSid():
	os.environ["account_sid"] = "ACe996d6fda1a47cadf642fe4cc3a929e2"

def setAuth():
	os.environ["auth_token"] =  "dd1a9f4ccbf9765b861009c6d36f0ec6"

def getSid():
	setSid()
	return os.environ.get("account_sid")	

def getAuth():
	setAuth()
	return os.environ.get("auth_token")	
# Your Account Sid and Auth Token from twilio.com/user/account

def message():
	msg = input("Please type your message here...\n")
	return msg

def send(msg):
	message = client.messages.create(
    "+919611485287",
    body= msg,
    from_="+18572142125",)
   # media_url="http://www.example.com/cheeseburger.png"
	print(message.sid)

account_sid = getSid()
auth_token = getAuth()
client = Client(account_sid, auth_token)
msg = message()
send(msg)