import requests
import sys

city = sys.argv[1]
API_END_POINT = f'https://api.pray.zone/v2/times/today.json?city={city}'


def get_todays_times():
    r = requests.get(API_END_POINT)
    # this returns a dictionary of prayer times
    # like :
    # {'Imsak': '04:05',
    #  'Sunrise': '05:34',
    #  'Fajr': '04:15',
    #  'Dhuhr': '11:56',
    #  'Asr': '15:28',
    #  'Sunset': '18:18',
    #  'Maghrib': '18:31',
    #  'Isha': '19:36',
    #  'Midnight': '23:16'}
    times = r.json()['results']['datetime'][0]['times']
    return times


def get_fajr() -> str:
    times = get_todays_times()
    return times['Fajr']


def get_dhuhr() -> str:
    times = get_todays_times()
    return times['Dhuhr']


def get_asr() -> str:
    times = get_todays_times()
    return times['Asr']


def get_maghrib() -> str:
    times = get_todays_times()
    return times['Maghrib']


def get_isha() -> str:
    times = get_todays_times()
    return times['Isha']


def get_prayer(name: str) -> str:
    times = get_todays_times()
    if name == 'Jumaa':
        name = 'Dhuhr'
    return times[name]
