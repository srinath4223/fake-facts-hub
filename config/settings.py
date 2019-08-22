from datetime import timedelta
import os

from datetime import timedelta
from distutils.util import strtobool


LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

SECRET_KEY = os.getenv('SECRET_KEY', None)

SERVER_NAME = os.getenv('SERVER_NAME',
                        'localhost:{0}'.format(os.getenv('DOCKER_WEB_PORT',
                                                         '8000')))

# SQLAlchemy.
pg_user = os.getenv('POSTGRES_USER', 'fakefacts')
pg_pass = os.getenv('POSTGRES_PASSWORD', 'password')
pg_host = os.getenv('POSTGRES_HOST', 'postgres')
pg_port = os.getenv('POSTGRES_PORT', '5432')
pg_db = os.getenv('POSTGRES_DB', pg_user)
db = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(pg_user, pg_pass,
                                               pg_host, pg_port, pg_db)
SQLALCHEMY_DATABASE_URI = db
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_USER_EMAIL = os.getenv('SEED_USER_EMAIL', 'dev@local.host')
SEED_USER_USERNAME = os.getenv('SEED_USER_USERNAME', 'dev')
SEED_USER_PASSWORD = os.getenv('SEED_USER_PASSWORD', 'password')

# Configure Pusher (you can leave the last 2 settings alone).
PUSHER_APP_ID = os.getenv('PUSHER_APP_ID', None)
PUSHER_KEY = os.getenv('PUSHER_KEY', None)
PUSHER_SECRET = os.getenv('PUSHER_SECRET', None)
PUSHER_CLUSTER = os.getenv('PUSHER_CLUSTER', 'us2')
PUSHER_SSL = True
PUSHER_AUTH_ENDPOINT = '/api/auth/pusher/'

# Allow browsers to securely persist auth tokens but also include it in the
# headers so that other clients can use the auth token too.
JWT_TOKEN_LOCATION = ['cookies', 'headers']

# Only allow JWT cookies to be sent over https. In production, this should
# likely be True.
JWT_COOKIE_SECURE = False

# When set to False, cookies will persist even after the browser is closed.
JWT_SESSION_COOKIE = False

# Expire tokens in 1 year (this is unrelated to the cookie's duration).
JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=52)

# We are authenticating with this auth token for a number of endpoints.
JWT_ACCESS_COOKIE_PATH = '/'

# Enable CSRF double submit protection. See this for a thorough
# explanation: http://www.redotheweb.com/2015/11/09/api-security.html
JWT_COOKIE_CSRF_PROTECT = True
