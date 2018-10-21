# cs3900_error_not_found
COMP3900 Major Project

## Instructions for SETTING UP the development environment.

Update/install virtualenv using pip: pip install virtualenv
```
virtualenv venv -p python3.6
```
Run the development environment:
```
source venv/bin/activate

pip install -r requirements.txt
```

Install the javascript dependencies
```
cd frontend

npm install
```

## Every time you add a python dependancy to the project, run:
```
pip freeze > requirements.txt
```

## Instructions for RUNNING the project locally.

#-------------------Note to TUTOR-------------------#

When we run “make” the command “python manage.py runserver &” does not stay run in the background. Can you please run “make”, then open a new terminal navigate to the root directory “cs3900_error_not_found”, then run this command “python manage.py runserver”.

OR

Please clone our git master branch. The makefile works there for some reason.

Sorry for the inconvenience.
Thank you.

#---------------------------------------------------#


After setting up the development environment & ensuring you've activated the v-env:
Change your directory back to the root directory (i.e. cs3900_error_not_found).

Give the script executable permission. (ONLY THE FIRST TIME)
```
chmod +x start.sh
```
Run the Script
```
make
```

If you would like to do this manually or the makefile did not work properly:

Run the following to make the database (ONLY THE FIRST TIME):
```
python manage.py makemigrations
python manage.py migrate
python importData.py
```

Run the following every time to run project locally:
```
python check_events.py &
python manage.py runserver &
```
Open new terminal, navigate to root directory (cs3900cs3900_error_not_found)
and activate virtual environment like you did above.
```
cd frontend
npm run dev &
```

Navigate to http://localhost:8080/

## Command for clearing Django DataBase
```
python manage.py flush
```

## To delete database and remake it

Delete the files:
0001_initial.py (any files with `<number`>\_initial.py)  
db.sqlite3

Then run:
```
python manage.py makemigrations 
python manage.py migrate 
python manage.py createsuperuser
python importData.py
```
