from setup.buildtheservice import service
from datetime import datetime, timedelta
from helpers import construct_start_and_end_time
from consts import TIMEZONE, CALENDAR_ID, PRAYERS


def get_event_by_name(name: str):
    calendar_id = 'primary'
    maxResults = 1
    q = name
    singleEvents = True
    # timeMin,timeMax are boundaries to get the event within the day
    # so the event returned is today's event
    timeMax = (datetime.now()).strftime("%Y-%m-%dT23:59:00Z")
    timeMin = (datetime.now()).strftime("%Y-%m-%dT00:00:00Z")
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
    if event['items'] != []:
        event_name = event['items'][0]['summary']
        new_start, new_end = construct_start_and_end_time(event_name)
        event_body = {
            'start': {'dateTime': new_start, 'timeZone': TIMEZONE},
            'end': {'dateTime': new_end, 'timeZone': TIMEZONE},
        }
        event_id = event['items'][0]['id']
        service.events().patch(calendarId=CALENDAR_ID, eventId=event_id, body=event_body).execute()
        print(f'{event_name} Updated Successfully.')


def create_event(name: str):
    new_start, new_end = construct_start_and_end_time(name)
    # colorId :
    # 1 -> Lavander
    # 2 -> Sage ( My color of choice for prayer events )
    # 3 -> Grape
    # 4 -> Flamingo
    # 5 -> banana
    # 6 -> Tangerine
    # 7 -> Peacock
    # 8 -> Graphite
    # 9 -> Blueberry
    # 10 -> Basil
    # 11 -> Tomato

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
        'colorId': '2'
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'{name} Event Created.')


def update_all_prayers():
    for prayer in PRAYERS:
        update_event(get_event_by_name(prayer))
    print('All Events updated.')
