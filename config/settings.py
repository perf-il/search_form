import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

DATABASE_NAME = os.getenv('DATABASE_NAME')

if os.getenv('DEBUG_MODE') == 'debug':
    DEBUG_MODE = True
else:
    DEBUG_MODE = False
