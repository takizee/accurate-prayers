import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
scopes = ['https://www.googleapis.com/auth/calendar']
script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
rel_path = "client-secrets.json"
abs_file_path = os.path.join(script_dir, rel_path)
client_secrets_file_path = os.path.join(script_dir, rel_path)
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file_path, scopes=scopes)
credentials = flow.run_console()
# you don't have to go for this process everytime  to get the credentials
# so you'll do it once and save the credentials you got.
# we'll dump it to a pickle file
pickle.dump(credentials, open("token.pkl", "wb"))
