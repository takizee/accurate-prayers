import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client-secrets.json", scopes=scopes)
credentials = flow.run_console()
# you don't have to go for this process everytime  to get the credentials
# so you'll do it once and save the credentials you got.
# we'll dump it to a pickle file
pickle.dump(credentials, open("token.pkl", "wb"))
