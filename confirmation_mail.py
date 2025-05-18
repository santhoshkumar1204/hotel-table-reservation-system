import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient_email, t_id, dat, tim):
    sender_email = 'royalembassy2024@gmail.com'
    sender_password = "gapsktibghhxswfc"  # Use an app-specific password if you have 2FA enabled
    subject = "This mail is to inform you that your booking at Royal Embassy is confirmed.Have a fine Dining!"
    body = (
        f"These are the details regarding your booking at our restaurant.We hope that you have a good experience and "
        f"come later in the future.\n\n\nTable ID:{t_id}\nDate of Booking:{dat}\nTime Of Booking:{tim}\n\n\nFor any "
        f"complaints regarding any facility at our restaurant,We are all ears to feedbacks and dont hesitate in "
        f"sending us a mail to RoyalEmbassy@gmail.com or call 9000135260.")
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()
        # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')


def send_email_admin(mail, t_id, dat, tim):
    sender_email = 'royalembassy2024@gmail.com'
    sender_password = 'gapsktibghhxswfc'  # Use an app-specific password if you have 2FA enabled
    recipient_email = "royalembassy2024@gmail.com"
    subject = "Table Booking"
    body = (
        f"UserMail: {mail}"
        f"\nTable ID:{t_id}\nDate of Booking:{dat}\n "
        f"Time Of Booking:{tim}"
    )
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()  # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
