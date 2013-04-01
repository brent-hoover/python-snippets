# [SNIPPET_NAME: Sending Email]
# [SNIPPET_CATEGORIES: smtplib, email]
# [SNIPPET_DESCRIPTION: Sending mail from gmail account with many attachements and to_many_mails_ids]
# [SNIPPET_AUTHOR: kutuma]
# [SNIPPET_LICENSE: GPL]
# [SNIPPET_UPLOADED_BY: Arulalan.T <tarulalan@gmail.com>]

# you need to set the gmail user name and its password at the line of 22 and 23 st (in gedit, line number) of this snippet.

# you need to set the to_mail_ids in a string array , subject, body , attachements_absolute_path in a string array from the line of 26 of this snippet.


#!/usr/bin/python
# ref : http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "username@gmail.com"
gmail_pwd = "gmail_password"


body=" I am Body "
subject="I   am     Subject "

to_mail_ids=["friend1_mail_id","friend2_mail_id"]
attachements_path=["absolute_attachement1_with_extension","absolute_attachement2_with_extension"]# for eg : /home/arul/z/nnk.txt, /home/arul/python/sam.py



def mail(to, subject, text, attach=[]):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   try:

		for i in range(len(attach)):
				part = MIMEBase('application', 'octet-stream')
				part.set_payload(open(attach[i], 'rb').read())
				Encoders.encode_base64(part)
				part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(str(attach[i])))
				msg.attach(part)
   except:
		print " The attachments doesnt exist in the path %s and %s" % (attach[0],attach[1])
			

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()



for to_mail_id in (to_mail_ids):
   mail(to_mail_id,
   subject,
   body,
   attachements_path)
   print "mail sent to :"+to_mail_id

print "\nmail sent successfully to all\n"
