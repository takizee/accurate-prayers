from datetime import datetime,timedelta

from consts import CALENDAR_ID, PRAYERS
from setup.buildtheservice import service
from times import get_prayer
def get_todays_events(type):
    """

    :param type:type of events either all events or just prayer events

    :returns: a list of todays events
    """
    calendar_id='primary'
    # singleEvents : set it to true to return just the event of the day
    # without it's recurring events
    singleEvents=True
    timeMax=(datetime.now()).strftime("%Y-%m-%dT23:59:00Z")
    timeMin=(datetime.now()).strftime("%Y-%m-%dT00:00:00Z")
    events = service.events().list(
        calendarId=CALENDAR_ID,
        singleEvents=singleEvents,
        timeMin=timeMin,
        timeMax=timeMax,
    ).execute()

    todays_events=[event['summary'] for event in events['items']]
    todays_prayers=[event['summary'] for event in events['items'] if event['summary'] in PRAYERS]
    if type=='a':
        return todays_events
    elif type=='p':
        return todays_prayers
def get_time_slices(name):
    """

    :param name: the name of the prayer we want its time
    :returns: returns a list of time slices year,month,day,hour,min
    """
    prayer_time=get_prayer(name)
    now=datetime.now()
    year=now.year
    month=now.month
    day=now.day
    hour,min=prayer_time.split(':')
    name_of_the_day = now.strftime('%A')
    return year,month,day,hour,min,name_of_the_day

def construct_start_and_end_time(name):
    """

    :param name: the name of the prayer
    :returns: start and end times of a given event
    """
    year,month,day,hour,minute,name_of_the_day=get_time_slices(name)
    new_start = f'{year}-{month}-{day}T{hour}:{minute}:00'
    tmp_end = datetime.strptime(new_start, '%Y-%m-%dT%H:%M:00')
    if name_of_the_day=='Friday':
        tmp_end_2 = tmp_end + timedelta(minutes=60)
    else:
        tmp_end_2 = tmp_end + timedelta(minutes=30)
    new_end = f'{tmp_end_2.year}-{tmp_end_2.month}-{tmp_end_2.day}T{tmp_end_2.hour}:{tmp_end_2.minute}:00'
    return new_start,new_end
