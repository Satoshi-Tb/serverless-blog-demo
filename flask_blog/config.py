DEBUG = True
DYNAMODB_REGION = "ap-northeast-1"
AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
DYNAMODB_ENDPOINT_URL = "http://localhost:8000"
SECRET_KEY = "secret key"
USERNAME = "john"
PASSWORD = "due123"

SESSION_TYPE = 'dynamodb'
SESSION_DYNAMODB_TABLE = 'serverless_blog_demo_sessions'
SESSION_DYNAMODB_REGION = DYNAMODB_REGION
SESSION_DYNAMODB_KEY_ID = AWS_ACCESS_KEY_ID
SESSION_DYNAMODB_SECRET = AWS_SECRET_ACCESS_KEY
SESSION_DYNAMODB_ENDPOINT_URL = DYNAMODB_ENDPOINT_URL
