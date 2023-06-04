import pyowm # Importing the pyowm module for weather data
from dotenv import load_dotenv
import os # Importing the os module to access the environment variables
load_dotenv() # Loading the environment variables
api_key = os.getenv('API_KEY')
owm = pyowm.OWM(api_key) # API key for the weather data
# This script is used to get the weather data from the API and display it in the terminal