# Query to validate if a user's email and username is unique
def validate_user(user_name=None, email=None):
  query = f"""
  SELECT person_id FROM `defaultdb`.Person P
  WHERE {f"(P.user_name = LOWER('{user_name}')" if user_name is not None else ''}
      {'OR' if user_name is not None and email is not None  else ''} {f"P.email = LOWER('{email}')" if email is not None else ''});
  """

  return query

# Query to retrive the person record - pass in only 
def get_person(key, value):
  query = f"""
  SELECT person_id, user_name, first_name, last_name, email FROM `defaultdb`.Person P
  WHERE {f"P.{key} = LOWER('{value}')"};
  """
  return query

# Query to get user_id and salt from user_name data on login
def get_person_auth(user_name):
  query = f"""SELECT P.* FROM `defaultdb`.Person P
  WHERE LOWER(user_name) = LOWER('{user_name}')
      OR LOWER(email) = LOWER('{user_name}');"""

  return query
