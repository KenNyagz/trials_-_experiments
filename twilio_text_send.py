from twilio.rest import Client

# Twilio credentials
account_sid = 'AC13f1d53cd3b04701e0e0fccd991ab2f3'
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Activate",
    from_='+254103654277',
    #from_='+254717044108',  # Your Twilio number
    to='+19723609222'      # Recipient's American number
)

print(f"Message sent with SID: {message.sid}")

