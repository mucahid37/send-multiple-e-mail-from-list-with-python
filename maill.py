import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.base import MIMEBase 

#The mail addresses and  password
sender_address = 'xxxx@xxxxxx.com' 
sender_pass = 'xxxxx'

#create mail html content list from html file
with open("index.html", "r", encoding='utf-8') as f:
    HtmlText= f.read()

#create mailing list from txt file
with open("mailler.txt", "r") as fd:
   lines = fd.read().splitlines()

# list of reciver email_id to the mail 
li = lines
length = len(li)

# Here we iterate the loop and send message one by one to the reciver
for i in range(length): 
    
    X = li[i]
    reciver_mail = X
    
    print(reciver_mail)
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] =  reciver_mail
    message['Subject'] =  'HERE MAİL SUBJECT'

    html = MIMEText(HtmlText, 'html')

    
    #The body and the attachments for the mail
    message.attach(html)

    #Create SMTP session for sending the mail
    s = smtplib.SMTP_SSL('smtp.yandex.com',465)
    s.ehlo()
    s.login(sender_address, sender_pass) 
    text = message.as_string()
    s.sendmail(sender_address, reciver_mail, text) 
    s.quit() 

    print(''+reciver_mail+' Mail Sent Successful!') 
