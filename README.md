# Update Prayer Times in Google Calendar API
This project is solving the problem of the continously changing prayer times.

the final result is a cron job that runs everyday to update the prayer times events in google calendar.

i'm planning to use 'Google Apps Script' to make it more user friendly without all the hustle of setting up the project,it'll be a simple Google Calendar Addon.


## Time Blocking Concept
The whole idea is the day is divided to 5 blocks :
* Fajr    -> Dhuhr
* Dhuhr   -> Asr
* Asr     -> Maghrib
* Maghrib -> Isha
* Isha    -> Fajr

And you fill in your tasks in these blocks.

Because all what matters is praying , anything else is a detail!

## Calendar Setup
Create five events in your calendar and name them as in the picture below.

Make them repeat daily.

![Before](images/before.png?raw=true "Before")

[comment]: <> (![After]&#40;images/after.png?raw=true "After"&#41; )

## Setup Environment and Dependencies
After activating your virtual environment , setup the dependencies from 'requirement.txt' 
```commandline
pip install -r requirements.txt
```
## Get Credintials
- run authflowsetup.py and follow the flow:
```commandline
python ./setup/authflowsetup.py
```
- follow the steps in the following pictures:
    * Ctrl+Click on the link
    ![click](images/click.png?raw=true "Before")
      
    * Choose email
  
    ![click](images/1.png?raw=true "Before")
  
    * Continue
    
    ![click](images/2.png?raw=true "Before")
  
    * Check and Continue

    ![click](images/3.png?raw=true "Before")
  
    * Copy this key and paste it in the command line
 
    ![click](images/4.png?raw=true "Before")

## Build the service
```commandline
python ./setup/buildtheservice.py
```

## Run the script
```commandline

```
## Create the Cron Job

    
