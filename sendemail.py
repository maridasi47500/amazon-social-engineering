import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line
import os

class Sendemail():
    def __init__(self, sender_email = os.environ["YOUR_EMAIL"], sender_name = os.environ["SENDERNAME"], password=os.environ["YOUR_PASSWORD"], receiver_emails = ["receiver1@email.com", "receiver2@email.com", "receiver3@email.com"], receiver_names=["receiver Name1", "receiver Name2", "receiver Name3"], filename = 'cat.gif', message="how are you"):
        # User configuration
        
        
        # Email body
        #email_html = open('email.html')
        #email_body = email_html.read()
        
        
        
        for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
                print("Sending the email...")
                # Configurating user's info
                msg = MIMEMultipart()
                msg['To'] = formataddr((receiver_name, receiver_email))
                msg['From'] = formataddr((sender_name, sender_email))
                msg['Subject'] = 'Hello, my friend ' + receiver_name
                email_body="""
                <html>
                <body>
                <h1>Hello, my friend {hello}</h1>
                <p>{msg}</p>
                <p>signé</p>
                <img src="cid:image1" />
                <p>anonyme</p>
                </body>
                </html>
                """.format(pic=filename,hello=receiver_name,msg=message)
        
                msg.attach(MIMEText(email_body, 'html'))
        
                try:
                    # Open PDF file in binary mode
                    with open(filename, "rb") as attachment:
                                    part = MIMEBase("application", "octet-stream")
                                    part.set_payload(attachment.read())
        
                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(part)
        
                    # Add header as key/value pair to attachment part
                    part.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {filename}",
                    )
                    part.add_header(
                            "Content-ID",
                            f"<image1>",
                    )
        
                    msg.attach(part)
                except Exception as e:
                        print(f'Oh no! We didnt found the attachment!n{e}')
                        break
        
                try:
                        # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        # Encrypts the email
                        context = ssl.create_default_context()
                        server.starttls(context=context)
                        # We log in into our Google account
                        server.login(sender_email, password)
                        # Sending email from sender, to receiver with the email body
                        
                        print(sender_email, receiver_email, msg.as_string())
                        server.sendmail(sender_email, receiver_email, msg.as_string())
                        
                        print('Email sent!')
                except Exception as e:
                        print(f'Oh no! Something bad happened!n{e}')
                        break
                finally:
                        print('Closing the server...')
                        server.quit()
        
