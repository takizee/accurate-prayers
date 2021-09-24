from setup.buildtheservice import service
from datetime import datetime,timedelta
from times import get_prayer

TIMEZONE = 'Africa/Cairo'
CALENDAR_ID='primary'

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
    if event['items']!=[]:
        event_name=event['items'][0]['summary']
        prayer_time=get_prayer(event_name)
        new_hour=prayer_time.split(":")[0]
        new_min=prayer_time.split(":")[1]
        now=datetime.now()
        new_start = f'{now.year}-{now.month}-{now.day}T{new_hour}:{new_min}:00'
        tmp_end = datetime.strptime(new_start, '%Y-%m-%dT%H:%M:00')
        if event_name=='Jumaa':
            tmp_end_2=tmp_end + timedelta(minutes=60)
        else:
            tmp_end_2 = tmp_end + timedelta(minutes=30)
        new_end = f'{tmp_end_2.year}-{tmp_end_2.month}-{tmp_end_2.day}T{tmp_end_2.hour}:{tmp_end_2.minute}:00'
        event_body = {
            'start': {'dateTime': new_start, 'timeZone': TIMEZONE},
            'end': {'dateTime': new_end, 'timeZone': TIMEZONE},
        }
        event_id=event['items'][0]['id']
        service.events().patch(calendarId=CALENDAR_ID,eventId=event_id,body=event_body).execute()

def update_all_prayers():
    prayers=['Fajr','Dhuhr','Jumaa','Asr','Maghrib','Isha']
    for prayer in prayers:
        update_event(get_event_by_name(prayer))






