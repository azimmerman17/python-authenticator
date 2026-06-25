from datetime import datetime, date

from app.extensions import db

# Model Contains Profile Information for Users
class Person(db.Model):
  __tablename__ = 'Person'
  person_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  user_name = db.Column(db.String(25), nullable=False, unique=True)
  first_name = db.Column(db.String(25), nullable=False)
  last_name = db.Column(db.String(25), nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  salt = db.Column(db.String(150), nullable=False)
  password_hash = db.Column(db.String(150), nullable=False)
  reset_token = db.Column(db.String(150), nullable=False)
  reset_expire = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
  created_at = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  updated_at = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())

  def __init__(self, **kwargs):
    super().__init__(**kwargs) 

  def as_dict(self):
    keys = ['salt', 'password_hash', 'reset_token', 'reset_expire', 'created_at', 'updated_at']
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in keys}

  def person_insert(self):
    query = f"""
      INSERT INTO `defaultdb`.Person (user_name, first_name, last_name, email, salt, password_hash, reset_token, reset_expire)
      VALUES (LOWER('{self.user_name}'), '{self.first_name}', '{self.last_name}', LOWER('{self.email}'), '{self.salt}', '{self.password_hash}', '{self.reset_token}', NOW());
    """

    return query

  def password_reset(self, token):
    query = f"""
      UPDATE `defaultdb`.`Person`
      SET reset_token = '{token}',
        reset_expire = NOW() + INTERVAL 30 MINUTE,
        updated_at = NOW()
      WHERE person_id = {self.person_id};
    """

    return query

  def update_password(self, password):
    query = f"""
      UPDATE `defaultdb`.`Person`
      SET password_hash = '{password}',
        reset_expire = NOW(),
        updated_at = NOW()
      WHERE person_id = {self.person_id};
    """
    
    return query

  def update_person(self, data):
    update_clause = ''

    for key in data:
      update_clause = f" {update_clause}, {key} = '{data[key]}'"

    query = f"""
      UPDATE `defaultdb`.`Person`
      SET updated_at = NOW()
        {update_clause}
      WHERE person_id = {self.person_id};
    """

    return query


