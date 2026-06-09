import  boto3
from dotenv import load_dotenv
import os

load_dotenv()
s3 = boto3.resource('s3')

bucket_name = os.getenv('BUCKET_NAME')
print("Wypisuje wszystkie S3 Buckety")
for bucket in s3.buckets.all():
    print(bucket.name)

print("Dodaje plik test.png do bucketu test-boto3-michalg")
try:
    with open('test.png', 'rb') as image_file:
        s3.Bucket('test-boto3-michalg').put_object(Key='test.png', Body=image_file)
        print("Plik test.png do bucketu test-boto3-michalg")
except:
    print("Nie udało się zaaplikować pliku test.png")