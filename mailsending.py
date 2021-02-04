import smtplib

sender = "arjunbaidya55@gmail.com"
recipient = "arjun.chandra.baidya@gmail.com"
password = "ramakrishna"
subject = "Test email from Python"
text = "Hello from Python"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()