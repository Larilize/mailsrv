import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

#sendmail('admin@example.com','SUBJECT','<h1>THIS IS MAIN TEXT</h1>','html','smtp.yourdomain.com',465,'hey@yourdomain.com','PASSWD')
def sendmail(to,subject,message,mailtype,hostname,port,frommail,passwd):
    msg = MIMEMultipart()
    msg['From'] = frommail
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, mailtype))
    try:
        server = smtplib.SMTP_SSL(hostname, port)
        server.login(frommail, passwd)
        server.sendmail(frommail, to, msg.as_string())
        server.quit()
        print('[OK] SENT MAIL TO ' + to + ' FROM ' + frommail )
    except smtplib.SMTPException as e:
        print('[NO] FAILED TO SENT MAIL TO ' + to + ' FROM ' + frommail )

from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['POST'])
def send_email():
    to = request.form['to']
    subject = request.form['subject']
    message = request.form['message']
    mailtype = request.form['mailtype']
    hostname = request.form['hostname']
    port = request.form['port']
    frommail = request.form['frommail']
    passwd = request.form['passwd']
    sendmail(to,subject,message,mailtype,hostname,port,frommail,passwd)
    return 'hello world'

if __name__ == '__main__':
    app.run(host='localhost', port=sys.argv[1])
    #app.run(host='localhost', 999)
