# email.py
import smtplib as smtp

from_addr = "david@onholdwizard.com"
to_addr = "guitardave@outlook.com"

smtpObj = smtp.SMTP("smtp.office365.com", 587)

smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(from_addr, "*7radio77*")
smtpObj.sendmail(from_addr, to_addr, "Subject: Gracias.\n\nThat was a great get-together. Had such fun")
smtpObj.quit()
print "success"