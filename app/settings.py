from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Database
DATA_PATH = os.environ.get("DATA_PATH")
DATA_File = os.environ.get("DATA_FILE")