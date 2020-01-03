import csv
import smtplib

port = 587
smtp_server = "smtp-mail.outlook.com"
login = "paulina.serotiuk@outlook.com"
password = "Paser666"

message = "This is a test email from Python - file version"
sender = login
with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(login, password)
    with open("/Users/paulinaserotiuk/Desktop/test_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        for email in reader:
            server.sendmail(sender, email, message)
        print('sukces!')

server.close()
