from setup.buildtheservice import service
from datetime import datetime,timedelta
from helpers import construct_start_and_end_time
from consts import TIMEZONE,CALENDAR_ID,PRAYERS



def get_event_by_name(name:str):
    calendar_id='primary'
    maxResults=1
    q=name
    singleEvents=True
    # timeMin,timeMax are boundaries to get the event within the day
    # so the event returned is today's event
    timeMax=(datetime.now()).strftime("%Y-%m-%dT23:59:00Z")
    timeMin=(datetime.now()).strftime("%Y-%m-%dT00:00:00Z")
    event = service.events().list(
        calendarId=CALENDAR_ID,
        maxResults=maxResults,
        q=name,
        singleEvents=singleEvents,
        timeMin=timeMin,
        timeMax=timeMax,
    ).execute()
    return event
def update_event(event):
    # check if the event searched for exists
    # e.g : in my calendar , there is no 'Fajr' event
    # so , if the event parameter is 'Fajr' , that means that -> event['items']==[]
    if event['items']!=[]:
        event_name=event['items'][0]['summary']
        new_start,new_end=construct_start_and_end_time(event_name)
        event_body = {
            'start': {'dateTime': new_start, 'timeZone': TIMEZONE},
            'end': {'dateTime': new_end, 'timeZone': TIMEZONE},
        }
        event_id=event['items'][0]['id']
        service.events().patch(calendarId=CALENDAR_ID,eventId=event_id,body=event_body).execute()



def create_event(name:str):
    # todo : create event
    new_start,new_end=construct_start_and_end_time(name)
    event = {
        'summary': name,
        'start': {
            'dateTime': new_start,
            'timeZone': TIMEZONE,
        },
        'end': {
            'dateTime': new_end,
            'timeZone': TIMEZONE,
        },
        'recurrence': [
            'RRULE:FREQ=DAILY'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 5},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
def update_all_prayers():
    for prayer in PRAYERS:
        update_event(get_event_by_name(prayer))







