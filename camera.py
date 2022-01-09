# Joseph Shepin
import os 
import boto3
from time import sleep
from datetime import datetime
from PIL import Image
from dotenv import load_dotenv

load_dotenv() #load in those env vars

photosTaken = 1
photoDelay = int(os.getenv('time_delay'))
maxPhotos = int(os.getenv('max_photos'))

def getTimeString():
    dateTime = str(datetime.now())
    return dateTime[0: dateTime.find(".")]


session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name=os.getenv('region_name')
)

client = boto3.client('s3')

while(photosTaken <= maxPhotos):
    print("taking photo %s/%s" % (photosTaken, maxPhotos))
    #take the image
    os.system('fswebcam -p YUYV -d /dev/video0 -r 1920x1080 --no-banner image.jpg')
    sleep(3) # time it takes for photo to be taken

    #compress the image
    filepath = os.path.join(os.getcwd(), "image.jpg")
    picture = Image.open(filepath)
    picture.save("image.jpg", "JPEG", optimize = True, quality = 50)

    #upload the image
    client.upload_file('image.jpg', os.getenv('S3_bucket'), getTimeString() + '.jpg')
    photosTaken+=1
    sleep(photoDelay - 3) # time in between photos

