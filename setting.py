import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
USER_ID = os.environ.get("USER_ID")
