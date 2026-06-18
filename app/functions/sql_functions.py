from datetime import datetime

# run a query
def run_query(query, conn=None, hide=True):
  from app.extensions import db, Engine
  flag = 0
  if conn == None:
    conn = Engine.connect()
    conn.begin()
    flag = 1

  # run the query
  try:
    result = conn.execute(db.text(query))
  except Exception as error:
    print('Exception', error)
    conn.rollback()
    conn.close()
    return error
  
  if hide == False:
    print('SQL QUERY:', query)

  if flag == 1:
    conn.commit()
    conn.close()

  return result

# check if connection is open
def check_conn(conn):
  try:
    conn.info
  except Exception as error:
    print(error)
    return 'error'
  
  return 'continue'
