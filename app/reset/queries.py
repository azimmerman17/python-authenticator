# Get person_id, first_name, and email for reseting the password
def get_person_request(data):
  query = f"""
    SELECT person_id, first_name, last_name, email FROM `defaultdb`.Person 
    WHERE LOWER(user_name) = LOWER('{data}')
      OR LOWER(email) = LOWER('{data}');
    """

  return query

# Get person_id and salt for reseting the password
def get_person_reset(person, token):
  query = f"""SELECT P.person_id, P.salt FROM `defaultdb`.Person P
      WHERE (LOWER(P.user_name) = LOWER('{person}')
          OR LOWER(P.email) = LOWER('{person}'))
        AND reset_token = '{token}'
        AND reset_expire > NOW();"""

  return query