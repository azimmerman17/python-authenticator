# Get user_id, first_name, and email for reseting the password
def get_user_reset(data):
  query = f"""
    SELECT person_id, first_name, last_name, email FROM `defaultdb`.Person 
    WHERE user_name = '{data}'
      OR email = '{data}';
    """

  return query