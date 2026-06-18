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
