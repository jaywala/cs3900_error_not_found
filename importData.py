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
    with open(abs_file_path, encoding = 'utf-8', mode = "r+") as csvfile:
        next(csvfile)
        readcsv = csv.reader(csvfile, delimiter=',')
        count = 0

        for row in readcsv:
            count += 1
            if count > 101:
                break

            user1 = User_Profile(user_name=row[21],name=row[21],email=(row[21]+"@example.com"),list_of_ads="1,")
            user1.save()
            print(count)
            amenitiestext = row[58]
            amenitiestext = amenitiestext.strip("{")
            amenitiestext = amenitiestext.strip("}")
            amenitiestext = amenitiestext.strip()
            amenitiestext = amenitiestext.replace('"', '')
            advertisement = Advertisement(
                ad_id=1,
                poster=(row[21]+"@example.com"),
                accommodation_name=row[4],
                accommodation_description=row[7],
                house_rules=row[14],
                base_price=float((row[60].strip("$")).replace(",","")),
                num_guests=int(row[65]),
                num_bedrooms=int(row[55]),
                num_bathrooms=int(float(row[54])),
                latitude=float(row[48]),
                longitude=float(row[49]),
                suburb=row[41],
                amenities=amenitiestext)
            advertisement.save()

if __name__ == '__main__':
    importFromCSV()
