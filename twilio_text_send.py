from twilio.rest import Client

# Twilio credentials
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Activate",
    from_='',  # Your Twilio number
    to=''      # Recipient's American number
)

print(f"Message sent with SID: {message.sid}")

