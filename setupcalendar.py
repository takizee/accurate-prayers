from helpers import get_todays_events
from event import create_event, update_event, get_event_by_name
from consts import CALENDAR_ID, TIMEZONE, PRAYERS


def setup_calendar():
    # get events of the day
    # create a list of all summaries
    # for each prayer :
    # if it doesn't exist in summaries : create it and make it repeat daily
    # if it does exist : update it
    # in the case of Dhuhr, if today is friday : name it Jumaa and make it
    # repeat weekly on friday
    todays_prayers = get_todays_events('p')
    for prayer in PRAYERS:
        if prayer not in todays_prayers:
            create_event(prayer)
        else:
            update_event(get_event_by_name(prayer))
    print("All Events Updated Successfully")
