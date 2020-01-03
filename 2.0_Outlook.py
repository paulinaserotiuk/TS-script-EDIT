import smtplib

#proces wysylania maili jest ok, ALE: nie ,moge zrobic tego z maila w domenie ergo ze wzgledu na 2 step authentication.
to = 'paulina.serotiuk@ergo.digital'
sender = 'paulina.serotiuk@outlook.com'
smtpserver = smtplib.SMTP('smtp-mail.outlook.com',587)
password = 'Paser666'
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(sender, password)
message = """\
Subject: Hi there

This message is sent from Python."""
smtpserver.sendmail(sender, to, message)
print('sukces')
smtpserver.close()
