import os
from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "ZwiipLo6S02ivZU-45kDBs8NpnfkyaK_YMeaB6fPrXEacXjz9hwAUWm6nl236UaCV6-kxA.",
    "__Secure-1PSIDTS" : "sidts-CjIBSAxbGTg8J3RSOgvaPvASJ1m7nBousDM79esUJ-o7wCKyXqxjbzO7LPJu6iWdqqmJnxAA",
    "__Secure-1PSIDCC" : "APoG2W-xwMIZolJwzQb60n_gD1pY7aPJQwlrOHbc5p7UR-UUXYfYqP-TRZgnX0S_Se1ec1gCaEg"
}

bard = BardCookies(cookie_dict=cookie_dict)

# Text Modification Function -
def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Image Detection

while True:
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename,'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "Brain\DataBase" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))
