import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
#zmienic na wczytywanie adresow z pliku
sender_email = "p.d.s.ergo@gmail.com"  # Enter your address
receiver_email = "paulina.serotiuk@ergo.digital"  # Enter receiver address
password = input("Type your password and press enter: ")
#zmienic tresc wiadomosci
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)