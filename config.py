# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
 
 
# Your Account Sid and Auth Token from twilio.com/console
ACCOUNT_SID = 'Your Account SID'

AUTH_TOKEN = 'Your Auth Token'

FROM_PHONE = "Your Phone_number"

client = Client(ACCOUNT_SID, AUTH_TOKEN)
