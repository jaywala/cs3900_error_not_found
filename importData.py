import os
import csv
import django
#import locale
#locale.setlocale(locale.LC_ALL, 'en_US.UTF8') # couldn't pip install this
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone.settings")

# First run django.setup()
django.setup()

# Import models
#from django.contrib.auth.models import User
from catalog.models import User_Profile, Advertisement




def deleteData():
    pass


def importFromCSV():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    #rel_path = "catalog/listings.csv"
    rel_path = "listings.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, encoding = 'utf-8', mode = "r+") as csvfile:
        next(csvfile)
        readcsv = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in readcsv:
            count += 1
            if count > 101:
                break
            # if row[4]  == "trainee":
            #     self._users.append(trainee(row[0],row[1],row[2],row[3]))
            # elif row[4] == "trainer":
            #     self._users.append(trainer(row[0],row[1],row[2],row[3]))
            #user = User.objects.create_user(username=row[21],email=(row[21]+"@example.com"),password="password")

            user1 = User_Profile(user_name=row[21],name=row[21],email=(row[21]+"@example.com"))
            user1.save()
            print(count)
            advertisement = Advertisement(user=user1,
                accommodation_name=row[4],
                accommodation_description=row[7],
                house_rules=row[14],
                #base_price=int(locale.atof(row[60].strip("$"))), # changed to FloatField in model.py
                base_price=float((row[60].strip("$")).replace(",","")), # need to get rid of commas as some of the prices are like $1,045.00
                num_guests=int(row[65]),
                num_bedrooms=int(row[55]),
                num_bathrooms=int(float(row[54])),
                latitude=float(row[48]),
                longitude=float(row[49]),
                suburb=row[42])
            advertisement.save()

if __name__ == '__main__':
    importFromCSV()
