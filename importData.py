import os
import csv
import django
import glob
import base64

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone.settings")

# First run django.setup()
django.setup()

# Import models
#from django.contrib.auth.models import User
from catalog.models import User_Profile, Advertisement, PropertyImage, Accommodation_Review


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

            print(count, "  " ,row[21])

            user1 = User_Profile(email=(row[21]+"@example.com"), # column V
                                 user_name=row[21],
                                 name=row[21],
                                 profile_pic="",
                                 list_of_ads="1,",
                                 list_of_rentals="",
                                 # (ad_owner, ad_id, rev_id); Since this is dummy data, they reviewed their own ad
                                 list_of_posted_reviews= "(" + row[21]+ "@example.com"  + "," + "1,1" + ");",
                                 )
            user1.save()

            amenitiestext = row[58] # column BG
            amenitiestext = amenitiestext.strip("{")
            amenitiestext = amenitiestext.strip("}")
            amenitiestext = amenitiestext.strip()
            amenitiestext = amenitiestext.replace('"', '')
            advertisement = Advertisement(
                ad_id=1,
                poster=(row[21]+"@example.com"),
                list_of_reviews="1,",
                list_of_events="",
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
                     ad_owner=(row[21]+"@example.com"),
                     ad_id=1,
                     # Since this is dummy data, they reviewed their own ad
                     reviewer= (row[21]+ "@example.com"),
                     rating=4,
                     message="",
                     )
            review.save()

            if count <= 2:
                im_number = 0
                filepath = 'accommodation_pics/' + str(count) + '/*.jpg'
                for filename in glob.glob(filepath):
                    im_number += 1
                    with open(filename,"rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        string = "data:image/jpeg;base64," + encoded_string.decode('UTF-8')
                    im = PropertyImage(image_id=im_number,
                                       ad_owner=(row[21]+"@example.com"),
                                       ad_id=1,
                                       pic=string)
                    im.save()

                temp_str = ""
                for i in range(1, im_number+1): # range(0,5) [0, 1, 2, 3, 4], so plus 1
                    temp_str = temp_str+ str(i) + ","
                advertisement.set_image_ids(temp_str)

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
