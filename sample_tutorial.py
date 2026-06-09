import boto3
from dotenv import load_dotenv
import os

load_dotenv()
bucket_name = os.getenv("BUCKET_NAME")

# Create S3 client with correct region (eu-west-2)
s3 = boto3.client('s3', region_name='eu-west-2')

# Fix: Disable public access blocks to allow presigned URLs to work
# print("Configuring bucket to allow presigned URL access...")
# try:
#     s3.put_public_access_block(
#         Bucket=bucket_name,
#         PublicAccessBlockConfiguration={
#             'BlockPublicAcls': False,
#             'IgnorePublicAcls': False,
#             'BlockPublicPolicy': False,
#             'RestrictPublicBuckets': False,
#         }
#     )
#     print("✓ Bucket configured successfully!\n")
# except Exception as e:
#     print(f"Note: {e}\n")

#List all the buckets
#
# buckets_response = s3.list_buckets()
# for bucket in buckets_response['Buckets']:
#     print(bucket)

#List all objects in bucket
# response = s3.list_objects_v2(Bucket=bucket_name)
# for object in response["Contents"]:
#     print(object["Key"])

#Upload a file to a bucket
# with open("./test.png", 'rb') as image_file:
#     s3.upload_fileobj(image_file, bucket_name, "test_nowy.png")
#     print("Plik test.png do bucketu", bucket_name)

#Download file from bucket
# s3.download_file(bucket_name, 'test_nowy.png', 'test_pobrany.png')

#Download file with binary data
# with open("downloaded_test.png", "wb") as f:
#     s3.download_fileobj(bucket_name, 'test_nowy.png', f)
    #Code here to send image to frontend

#Presigned URL to give limited access to specified user
# url = s3.generate_presigned_url("get_object", Params={"Bucket": bucket_name, "Key": "test_with_default_access.png"}, ExpiresIn=30)
# print(url)

#Create bucket
# bucket_location = s3.create_bucket(
#     Bucket="new-destination-bucket-michalg",
#     CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'} #Bo nie korzystam z ue-east-1
# )
# print(bucket_location)

#Copy Objects between Buckets
# s3.copy_object(
#     Bucket="new-destination-bucket-michalg",
#     CopySource=f"/{bucket_name}/test_nowy.png",
#     Key="Coppied_test.png"
# )

#Get details of obect

# response = s3.get_object(Bucket=bucket_name, Key='test_nowy.png')
# print(response)