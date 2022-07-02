import uuid
from lib import db

db_client = db.dynamodb_client

USERS_TABLE = os.environ['USERS_TABLE']

def generate_user_id():
  return uuid.uuid4()

def get_user_from_db(user_id):
  result = db_client.get_item(
    TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
  )
  item = result.get('Item')
  return item

def create_user_in_db(name, age):
  user_id = generate_user_id()
  item = { 'userId': {'S': user_id }, 'name': { 'S': name }, 'age': { 'N': age } }
  db_client.put_item(TableName=USERS_TABLE, Item=item)