from flask import request
from markupsafe import escape
from datetime import datetime, timedelta
from ua_parser import parse_os, parse_device, parse

from app.reset import bp
from app.reset.queries import get_user_reset
from app.reset.functions import generate_reset_token
from app.models.person import Person
from app.functions.sql_functions import run_query
from app.email.reset_email.html import reset_password_email
from app.email.functions import send_email
from config import Config

# request for a password reset
@bp.route('/request', methods=['POST'])
def request_reset(config_class=Config):
  # define request user agent
  ua = request.headers['User-Agent']
  
  # TESTING IN POSTMAN
  if config_class.ENV == 'TEST':
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36' 
 
  parsed_ua = parse(ua)
  
  browser = parsed_ua.user_agent.family if parsed_ua.user_agent.family != None else 'Unknown'
  os = parsed_ua.os.family if parsed_ua.os.family != None else 'Unknown'
  device = parsed_ua.device.family if parsed_ua.device.family != None else 'Unknown'
  
  
  # get user informtion
  try:
    person_info = request.json['user_info'] #if
    person_query = get_user_reset(person_info)
    person = run_query(person_query).mappings().all()

    if len(person) != 1:
      print('ERROR - incorrect number of rows returned')
      return {'msg': 'Unable to validate the user exists'}, 500

    person = Person(person_id=person[0]['person_id'], first_name=person[0]['first_name'], last_name=person[0]['last_name'], email=person[0]['email'])
    person_dict = person.as_dict()
  except Exception as error:
    print('ERROR - ', error)
    return {'msg': 'Unable to validate the user'}, 500

  try:
    # generate reset tokens
    token, hashted_token = generate_reset_token()
    
    # update reset token in DB
    run_query(person.password_reset(hashted_token))

    # generate reset email
    email_html = reset_password_email(person_dict, token, os, browser, request.json['app'])
    payload = {
      'subject': f'Requested password reset for {request.json['app']['company']}',
      'from': config_class.MAIL_USERNAME,
      'to': person_dict['email'] if config_class.ENV == 'PROD' else config_class.MAIL_USERNAME,
      'html': email_html
    }
    send_email(payload, config_class)

    return {'msg': 'reset email process complete'}, 200
  except Exception as error:
    print('ERROR - ', error)
    return {'msg': 'Unable to generate reset token'}, 500

