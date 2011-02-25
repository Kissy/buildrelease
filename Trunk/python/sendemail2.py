import sys
import os.path
import smtplib
import email  
import mimetypes

from email import encoders
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

  
def sendMail(mailhost,subject,sender,recipients,ccto = '',bccto = '',message = '', payloads = ''):
  try:
    mailport=smtplib.SMTP(mailhost)
  except:
    sys.stderr.write('Unable to connect to SMTP host "' + mailhost \
                      + '"!\nYou can try again later\n')
    return 0
    
  msgroot = MIMEMultipart('mixed')
  msgroot['From'] = sender
  msgroot['To'] = recipients
  msgroot['Cc'] = ccto
  msgroot['Bcc'] = bccto
  msgroot['Subject'] = subject

  alternative = MIMEMultipart('alternative')
  msgroot.attach(alternative)  
  mes = MIMEText(message,'plain','utf-8')
  alternative.attach(mes)
    
  for file in payloads.split(','):
      if os.path.isfile(file) and os.path.exists(file):
        msgroot.attach(getMIMEObj(file))
      else:
        sys.stderr.write("The file %s cannot be found" % file)
  
  try:
    #mailport.set_debuglevel(1)
    allrecipients = recipients.split(',')
    if not ccto == '':
      allrecipients.extend(ccto.split(',')) 
    if not bccto == '':
      allrecipients.extend(bccto.split(',')) 
    #print allrecipients
    failed = mailport.sendmail(sender, allrecipients, msgroot.as_string())
    if failed == None:
      sys.stderr.write(failed)
      return 0
  except Exception as e:
    sys.stderr.write(repr(e))
    return 0
  finally:
    mailport.quit()
    
  return 1


mailhost = 'mail-relay.company.com'
sender  = "AAA@Company.com"
recipients = "BBB@company.com"
ccto = 'CCC@company.com'
bccto = 'DDD@company.com'
subject = "Testing1"
message = "Testing!\nTesting!\n"     

sendMail(mailhost,subject,sender,recipients,message = message,payloads = 'c:\\test\\test.ba,C:\\test\s7\\mytable.txt')