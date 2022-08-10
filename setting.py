import os
from dotenv import load_dotenv
import json
load_dotenv()
DB_INFO = json.loads(os.getenv("DB_INFO"))

API_SECURITY_INFO = json.loads(os.getenv("API_SECURITY_INFO"))
API_SECRET_KEY = API_SECURITY_INFO.get("secret_key")
API_ALGORITHM = API_SECURITY_INFO.get("algorithm")
API_ACCESS_TOKEN_EXPIRE_MINUTES = API_SECURITY_INFO.get("access_token_expire_minutes")

AWS_SECURITY_INFO = json.loads(os.getenv("AWS_SECURITY_INFO"))
AWS_REGION_NAME = AWS_SECURITY_INFO.get("region_name")
AWS_ACCESS_KEY_ID = AWS_SECURITY_INFO.get("aws_access_key_id")
AWS_SECRET_ACCESS_KEY = AWS_SECURITY_INFO.get("aws_secret_access_key")

DB_USERNAME = DB_INFO.get("username")
DB_PASSWORD = DB_INFO.get("password")
DB_HOST = DB_INFO.get("host")
DB_PORT = DB_INFO.get("port")
DB_REPLICA_SET = DB_INFO.get("replica_set")
DB_AUTHENTICATION_MECHANISM = DB_INFO.get("authentication_mechanism")
DB_AUTHENTICATION_SOURCE = DB_INFO.get('authentication_source')
MONGODB_URL = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authSource={DB_AUTHENTICATION_SOURCE}&replicaSet={DB_REPLICA_SET}&readPreference=primary&directConnection=true&ssl=false"
ACCOUNT_AVAILABLE_INTERVAL_FROM_LAST_LOGIN = int(os.getenv('ACCOUNT_AVAILABLE_INTERVAL_FROM_LAST_LOGIN'))

IS_WINDOWS = bool(int(os.getenv('IS_WINDOWS')))
ACCEPTED_CLIENT_HOST = json.loads(os.getenv("ACCEPTED_CLIENT_HOST"))
TEST_ACCEPTED_CLIENT_HOST = json.loads(os.getenv("TEST_ACCEPTED_CLIENT_HOST"))