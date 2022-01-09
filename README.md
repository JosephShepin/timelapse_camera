# Timelapse Snapshot Program Using Amazon S3

Install pip packages
`pip3 install -r requirements.txt`

Install fswebcam
`sudo apt install fswebcam`

Duplicate `.env-template` and rename it to `.env`, and insert AWS credentials.

Environment Variables
`time_delay`delay between when photos are taken, measured in seconds. This must be at least 3.
`max_photos` the total of photos that want to be taken.

If you set `time_delay` to 60, and `max_photos` to 1440, then an entire day will be captured with a photo taken every minute. 

Images are also compressed 50% by default. This can be adjusted for varying levels of quality and desired file sizes.  