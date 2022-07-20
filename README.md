# Productive Muslim
![click](images/cover.png?raw=true "Alert")

Google Calendar Addon to create and updates prayer times events to help muslims organize their day using the Time Blocking technique.

> Time blocking is a time management method that asks you to divide your day into blocks of time. Each block is dedicated to accomplishing a specific task, or group of tasks, and only those specific tasks. Instead of keeping an open-ended to-do list of things you’ll get to as you’re able, you’ll start each day with a concrete schedule that lays out what you’ll work on and when.

# Concept
The idea behind this time management technique is to organize your productivity sessions so that each session begins and ends with a prayer.

# Day Structure
The day is structured as time blocks between prayers (Fard and sunnah) 

1- after fajr -> duha [ 3 hours on average depending on when you're going to pray duha]

2- duha -> dhuhr [ 3 hours ]

3- dhuhr -> asr [ 3 hours ]

4- asr ->maghrib [3 hours ]

5- maghrib -> isha [ 1 hour ]

6- isha -> witr [ 2 hours ]


Note that the duration of each block is not fixed as prayer times changes , blocks will be shorter in winter than summer.


# Note
i'm planning to use 'Google Apps Script' to make it more user friendly without all the hustle of setting up the
project,it'll be a simple Google Calendar Addon.

```diff
- This app is under verification by Google's Safety,so you have to cantact me  to add your account to the test users
- click on Advanced and send me an email with your Gmail in it .
```

![click](images/0.png?raw=true "Alert")

# Installation

## Cloning 
To clone the repo run:
```commandline
git clone https://github.com/takizee/accurate-prayers.git
```
## Dependencies

* Create the virtual environment , if you prefer virtualenv run:
```commandline
virtualenv accurate-prayers
```
then activate it :
```commandline
source ./accurate-prayers/bin/activate
```
* Install the dependencies:
```commandline
pip install -r requirements.txt
```

## Get Credintials

- run authflowsetup.py and follow the flow:

```commandline
python ./setup/authflowsetup.py
```

- follow the steps in the following pictures:
    * Ctrl+Click on the link appeared in your terminal , as in the picture below 
      ![click](images/click.png?raw=true "Before")

    * Choose email
    

  ![click](images/1.png?raw=true "Before")

    * Continue
    

  ![click](images/2.png?raw=true "Before")

    * Check and Continue
    

  ![click](images/3.png?raw=true "Before")

    * Copy this code and paste it in the terminal 
    

  ![click](images/4.png?raw=true "Before")

## Build the service

```commandline
python ./setup/buildtheservice.py
```

## Run the script

```commandline
python app.py [city]
```

Replace [city] with your city. here is a list of famous cities:

cairo,alexandria,giza,asyut

Or you could refrence this page and search for your city.


https://ask-aladdin.com/egypt-cities/

NOTE: The API supports all countries in the world not just egypt.

<!-- ## Create the Cron Job

    
To create a cron job to run this script daily ,follow the following steps:
* in your terminal type:
```commandline
crontab -e
```
* choose your favourite text editor ( I personally prefer vim)
* A text file will open , insert the following cronjob in a new line in the file.
```commandline
@daily /path/to/your/virtual/environment/bin/python /path/to/your/project/directory/app.py [city]
```
if you're using virtualenv for example , your python interpter will be located at ~/.virtualenvs/name-of-the-environment/bin/python
 -->
