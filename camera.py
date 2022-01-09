import os 
import boto3
from time import sleep
from datetime import datetime
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

def getTimeString():
    dateTime = str(datetime.now())
    return dateTime[0: dateTime.find(".")]


session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key')
    region_name=os.getenv('region_name')
)

client = boto3.client('s3')

#take the image
os.system('fswebcam -r 1920x1080 --no-banner image.jpg')
sleep(5)

#compress the image
filepath = os.path.join(os.getcwd(), "image.jpg")
picture = Image.open(filepath)
picture.save("image.jpg", "JPEG", optimize = True, quality = 50)

#upload the image
client.upload_file('image.jpg', os.getenv('S3_bucket'), getTimeString() + '.jpg')

