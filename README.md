# cs3900_error_not_found
COMP3900 Major Project

## Instructions for SETTING UP the development environment.
Update/install virtualenv using pip: pip install virtualenv

1. virtualenv venv -p python3.6
2. source venv/bin/activate
3. pip install -r requirements.txt

4. cd frontend
5. npm install


## Instructions for RUNNING the project locally.
After setting up the development environment & ensuring you've activated the v-env:

1. python manage.py runserver &
2. cd frontend
3. npm run dev &

## Command for clearing Django DataBase
python manage.py flush

Navigate to http://localhost:8080/

## To delete database and remake it

Delete the files:
0001_initial.py (any files with '<number'>\_initial.py)  
db.sqlite3

Then run:
1. python manage.py makemigrations 
2. python manage.py migrate 
3. python manage.py createsuperuser
4. python importData.py
