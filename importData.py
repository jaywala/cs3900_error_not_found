import os
import csv
import django

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
    with open(abs_file_path) as csvfile:
        next(csvfile)
        readcsv = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in readcsv:
            count += 1
            if count > 100:
                break
            # if row[4]  == "trainee":
            #     self._users.append(trainee(row[0],row[1],row[2],row[3]))
            # elif row[4] == "trainer":
            #     self._users.append(trainer(row[0],row[1],row[2],row[3]))
            #user = User.objects.create_user(username=row[21],email=(row[21]+"@example.com"),password="password")
            '''
            user = User_Profile(user_name=row[21],name=row[21],email=(row[21]+"@example.com"))
            advertisement = Advertisement(User_Profile=user,
                accommodation_name=row[4],
                accommodation_description=row[7],
                house_rules=row[14],base_price=row[34],
                num_guests=row[39],
                num_bedrooms=row[56],
                num_bathrooms=row[55],
                suburb=row[42])
            '''
            #print(row[21])
            #break

if __name__ == '__main__':
    importFromCSV()
