from googleapiclient.discovery import build
import pickle
import os

script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
rel_path = "token.pkl"
abs_file_path = os.path.join(script_dir, rel_path)
credentials_file_path = os.path.join(script_dir, rel_path)
credentials = pickle.load(open(credentials_file_path, "rb"))
service = build("calendar", "v3", credentials=credentials)
print('Service Created For Google Calendar API')
