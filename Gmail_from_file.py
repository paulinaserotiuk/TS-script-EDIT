import csv
import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp.gmail.com"
login = "p.d.s.ergo@gmail.com"
password = "Paser666"

#message = """
#Subject: Timesheet reminder
#Dear Ergonaut,
#This is a reminder to fill you timesheet
#"""

message = MIMEText('This is test mail')
message['Subject'] = 'Test mail about timesheets'

sender = login
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()
    server.login(login, password)
    #tu musze podmienic plik za kazdym razem
    with open("/Users/paulinaserotiuk/Desktop/test_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        for email in reader:
            server.sendmail(sender, email, message.as_string())
        print('sukces!')

server.close()


