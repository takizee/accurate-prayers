# Update Prayer Times in Google Calendar
```diff
- This app is under verification by Google's Safety,so you have to cantact me  to add your account to the test users
- click on Advanced and send me an email with your Gmail in it .
```

![click](images/0.png?raw=true "Alert")

This project is solving the problem of the continously changing prayer times.

the final result is a cron job that runs everyday to update the prayer times events in google calendar.

i'm planning to use 'Google Apps Script' to make it more user friendly without all the hustle of setting up the
project,it'll be a simple Google Calendar Addon.

## Time Blocking Concept

The whole idea is the day is divided to 5 blocks :

* Fajr -> Dhuhr
* Dhuhr -> Asr
* Asr -> Maghrib
* Maghrib -> Isha
* Isha -> Fajr

And you fill in your tasks in these blocks.

Because all what matters is praying , anything else is a detail!

[comment]: <> (## Calendar Setup)

[comment]: <> (Create five events in your calendar and name them as in the picture below.)

[comment]: <> (Make them repeat daily.)

[comment]: <> (![Before]&#40;images/before.png?raw=true "Before"&#41;)

[comment]: <> (![After]&#40;images/after.png?raw=true "After"&#41; )

## Cloning 
To clone the repo run:
```commandline
git clone https://github.com/takizee/accurate-prayers.git
```
## Setup Environment and Dependencies

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

## Create the Cron Job

    
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



