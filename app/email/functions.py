import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(payload, CONFIG):
  # print(payload)

  # define connection varibles
  mail_server = CONFIG.MAIL_SERVER
  port = CONFIG.MAIL_PORT
  username = CONFIG.MAIL_USERNAME
  password = CONFIG.MAIL_PASSWORD

  # Build email message
  message = MIMEMultipart('alternative' )
  message['subject'] = payload['subject']
  message['from'] = username
  message['to'] = payload['to']  if 'to' in payload.keys() else ''
  message["bcc"] = payload['bcc']  if 'bcc' in payload.keys() else ''
  message.attach(MIMEText(payload['html'], 'html'))

  try:
    # connent to the mail server and send email
    with smtplib.SMTP(f'{mail_server}:{port}') as server:
      server.starttls()
      server.login(username, password)
      server.sendmail(username, payload['to'], message.as_string())
  except Exception as e:
    # Print any error messages
    print('Error: ', e)
   