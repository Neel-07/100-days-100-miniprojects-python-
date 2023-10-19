import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and recipient email addresses
sender_email = "your_email@gmail.com"
recipient_email = "recipient_email@example.com"
password = "your_password"

# Create a message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Automated Email"

# Email content
body = "This is an automated email sent using Python. You can customize this text."
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server (Gmail)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
