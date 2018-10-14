import os
import csv
import django
import glob
import base64
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone.settings")

# First run django.setup()
django.setup()

# Import models
#from django.contrib.auth.models import User
from catalog.models import User_Profile, Advertisement, PropertyImage
from catalog.models import Accommodation_Review, Event, PropertyRequest

from datetime import datetime, time

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
            if count == 100:
                break

            # added a number to the end of the name to take care of duplicate users
            email = row[21].lower() + str(count)
            print(count, "  " , email)

            user1 = User_Profile(email=(email.replace(" ", "")+"@example.com"), # column V
                                 user_name=email,
                                 name=email,
                                 profile_pic="",
                                 list_of_ads="1,",
                                 list_of_rentals= "(" + email.replace(" ", "") + "@example.com,1,1);",
                                 # (ad_owner, ad_id, rev_id); Since this is dummy data, they reviewed their own ad
                                 list_of_posted_reviews= "(" + email.replace(" ", "") + "@example.com,1,1);",
                                 )
            user1.save()

            amenitiestext = row[58] # column BG
            amenitiestext = amenitiestext.strip("{")
            amenitiestext = amenitiestext.strip("}")
            amenitiestext = amenitiestext.strip()
            amenitiestext = amenitiestext.replace('"', '')
            advertisement = Advertisement(
                ad_id=1,
                poster=(email.replace(" ", "")+"@example.com"),
                poster_id=user1.id, 
                list_of_reviews="1,",
                list_of_events="1,",
                list_of_images="",
                accommodation_name=row[4], # column E
                accommodation_description=row[7], # column H
                property_type=row[51], # column AZ
                house_rules=row[14], # column O
                booking_rules="no cancellation",
                amenities=amenitiestext,
                base_price=float((row[60].strip("$")).replace(",","")), # column BI
                num_guests=int(row[65]), # column BN
                num_bedrooms=int(row[55]), # column BD
                num_bathrooms=int(float(row[54])), # column BC
                address=str(row[41]), # column AP
                city=row[45], # column AT
                zip_code=row[43], # column AR
                latitude=float(row[48]), # column AW
                longitude=float(row[49]), # column AX
                )
            advertisement.save()

            review = Accommodation_Review(
                     rev_id=1,
                     ad_owner=(email.replace(" ", "")+"@example.com"),
                     ad_id=1,
                     # Since this is dummy data, they reviewed their own ad
                     reviewer= (email.replace(" ", "")+ "@example.com"),
                     rating=4,
                     message="Good holiday home",
                     )
            review.save()


            month = random.randint(1, 12) # [1,13) non-inclusive last number

            if month < 10:
                month = "0" + str(month)

            s_str = "2018-" + str(month) + "-01"
            e_str = "2018-" + str(month) + "-05"

            start_day = datetime.strptime(s_str, "%Y-%m-%d").date()
            end_day = datetime.strptime(e_str, "%Y-%m-%d").date()

            start_day_start_time = datetime.strptime("00:00:00", "%H:%M:%S").time()
            end_day_end_time = datetime.strptime("00:00:00", "%H:%M:%S").time()

            event = Event(
                    event_id=1,
                    ad_owner=(email.replace(" ", "")+"@example.com"),
                    ad_id=1,
                    # Since this is dummy data, the owner booked their own property
                    booker=(email.replace(" ", "")+"@example.com"),
                    start_day=start_day,
                    start_day_start_time=start_day_start_time,
                    end_day=end_day,
                    end_day_end_time=end_day_end_time,
                    booking_status="booked",
                    notes="I'm bringing a dog =)",
                    )
            event.save()

            if count <= 100:
                im_number = 0
                filepath = 'accommodation_pics/' + str(count) + '/*.jpg'
                for filename in glob.glob(filepath):
                    im_number += 1
                    with open(filename,"rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        string = "data:image/jpeg;base64," + encoded_string.decode('UTF-8')
                    im = PropertyImage(image_id=im_number,
                                       ad_owner=(email.replace(" ", "")+"@example.com"),
                                       ad_id=1,
                                       pic=string)
                    im.save()

                temp_str = ""
                for i in range(1, im_number+1): # range(0,5) [0, 1, 2, 3, 4], so plus 1
                    temp_str = temp_str+ str(i) + ","
                advertisement.set_image_ids(temp_str)

    list_of_names = ['abbey', 'bob', 'cathy', 'dug', 'erin']
    for i in range(5):
        p = PropertyRequest(
                name=list_of_names[i],
                email=list_of_names[i].replace(" ", "")+"@example.com",
                text="I need a home. (NOTE: this is dummy data)"
            )
        p.save()

def importImages():
    # import images
    i = 1
    count = 0
    for i in range (1,3):
        filepath = 'accommodation_pics/' + str(i) + '/*.jpg'
        for filename in glob.glob(filepath):
            if count == 1:
                break
            count+=1
            with open(filename,"rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                strin = encoded_string.decode('UTF-8')
                print(type(strin))
                print(len(strin))




if __name__ == '__main__':
    importFromCSV()
    # importImages()
