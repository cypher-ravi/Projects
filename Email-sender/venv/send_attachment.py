# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "ronniloreo@gmail.com"
to_addr = "manavpawar6749@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = from_addr

# storing the receivers email address
msg['To'] = to_addr

# storing the subject
msg['Subject'] = "Test mail"

# string to store the body of the mail
body = "List of students"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "database.csv"
attachment = open("database.csv", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(from_addr, "ronniloreo@123")

# Converts the Multipart msg into a string
text = msg.as_string()
print('all good boss!!')

# sending the mail
s.sendmail(from_addr, to_addr, text)

# terminating the session
s.quit()
