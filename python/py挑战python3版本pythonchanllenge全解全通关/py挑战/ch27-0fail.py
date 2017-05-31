#coding=gbk
#目标机器积极拒绝,不懂了
import smtplib
from email.message import Message
apology = Message()
apology.add_header('To', 'leopold.moz@pythonchallenge.com')
apology.add_header('From', "youraddress@com.com")
apology.add_header('Subject', 'Apology')
apology.set_payload('Sorry!')
print (apology.as_string())
server = smtplib.SMTP('pythonchallenge.com')
server.sendmail(apology['from'], apology['to'], apology.as_string())
server.quit()
