﻿import sys
import os.path
import smtplib
import email

def sendTextMail(mailhost,sender,recipients,ccto = '',bccto = '',subject = '',message = '', messagefile = ''):

  try:
    mailport=smtplib.SMTP(mailhost)
  except:
    sys.stderr.write('Unable to connect to SMTP host "' + mailhost \
                      + '"!\nYou can try again later\n')
    return 0
    
  if(os.path.exists(messagefile) and os.path.isfile(messagefile)):
    with open(messagefile,'r') as f:
      message += f.read()
    
  fullmessage = 'From: ' + ' <' + sender + '> \n' +\
              'To: ' + recipients + '\n' +\
              'CC: '+ ccto + '\n' +\
              'Bcc: ' + bccto + '\n' +\
              'Subject: ' + subject + '\n' +\
              'Date: ' + email.Utils.formatdate() +'\n' +\
              '\n' +\
              message

  try:
    #mailport.set_debuglevel(1)
    allrecipients = recipients.split(',')
    if not ccto == '':
      allrecipients.extend(ccto.split(',')) 
    if not bccto == '':
      allrecipients.extend(bccto.split(',')) 
    #print allrecipients
    #allrecipients must be list type
    failed = mailport.sendmail(sender, allrecipients, fullmessage)
  except Exception as e:
    sys.stderr.write(repr(e))
    return 0
  finally:
    mailport.quit()
    
  return 1
  
  
from email import encoders
import mimetypes
from email.mime.base import MIMEBase
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def getMIMEObj(path):
    ctype, encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    msg = None
    #print maintype 
    #print subtype
    if maintype == 'text':
        fp = open(path)
        # Note: we should handle calculating the charset
        msg = MIMEText(fp.read(), _subtype=subtype, _charset='utf-8')
        fp.close()
    elif maintype == 'image':
        fp = open(path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(path, 'rb')
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        encoders.encode_base64(msg)
    # Set the filename parameter
    msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
    return msg

  
def sendHtmlMail(mailhost,subject,sender,recipients,ccto = '',bccto = '',htmldir = '', htmlfile = ''):
  try:
    mailport=smtplib.SMTP(mailhost)
  except:
    sys.stderr.write('Unable to connect to SMTP host "' + mailhost \
                      + '"!\nYou can try again later\n')
    return 0
    
  msgroot = MIMEMultipart('related')
  msgroot['From'] = sender
  msgroot['To'] = recipients
  msgroot['Cc'] = ccto
  msgroot['Bcc'] = bccto
  msgroot['Subject'] = subject

  msghtml = MIMEMultipart('alternative')
  msgroot.attach(msghtml)  
  if os.path.exists(os.path.join(htmldir,htmlfile)):
    htmlf = open(os.path.join(htmldir,htmlfile))
    htmlmessage = MIMEText(htmlf.read(),'html','utf-8')
    htmlf.close()
    msghtml.attach(htmlmessage)
    
  for root, subdirs, files in os.walk(htmldir):
    for file in files:
      if file == htmlfile:
        continue
      else:
        msgroot.attach(getMIMEObj(os.path.join(root,file)))
  
  failed = 0
  try:
    #mailport.set_debuglevel(1)
    allrecipients = recipients.split(',')
    if not ccto == '':
      allrecipients.extend(ccto.split(',')) 
    if not bccto == '':
      allrecipients.extend(bccto.split(',')) 
    #print allrecipients
    failed = mailport.sendmail(sender, allrecipients, msgroot.as_string())
    print failed
  except Exception as e:
    sys.stderr.write(repr(e))
  finally:
    mailport.quit()
    
  return failed    


mailhost = 'mail-relay.example.com'
sender  = "AAA@example.com"
recipients = "BBB@example.com,EEE@example.com"
ccto = 'CCC@example.com'
bccto = 'DDD@example.com'
subject = "Testing1"
message = "Testing!\nTesting!\n"
messagefile = "mymessage.txt"
htmldir = 'D:\\html'
htmlfile = 'myhtmleamil.html'
          
sendTextMail(mailhost,sender,recipients,ccto,bccto,subject,message,messagefile)
sendHtmlMail(mailhost, subject,sender,recipients,htmldir=htmldir,htmlfile=htmlfile)
