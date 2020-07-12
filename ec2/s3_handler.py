import boto3
from botocore.client import Config


class S3Handler:
    ACCESS_KEY_ID = 'ACCESS_KEY_ID'
    ACCESS_SECRET_KEY = 'ACCESS_SECRET_KEY'
    BUCKET_NAME = 'BUCKET_NAME'

    def __init__(self):
        s3 = boto3.resource(
            's3',
            aws_access_key_id=self.ACCESS_KEY_ID,
            aws_secret_access_key=self.ACCESS_SECRET_KEY,
            config=Config(signature_version='s3v4')
        )
        self.file_bucket = s3.Bucket(self.BUCKET_NAME)

    def upload_file(self, file_path, directory=None):
        s3_path = file_path
        if directory:
            s3_path = directory + '/' + file_path
        with open(file_path, 'rb') as data:
            self.file_bucket.put_object(
                Key=s3_path,
                Body=data)

    def get_file_urls(self, directory):
        result = {}
        for s3_object in self.file_bucket.objects.filter(Prefix=directory):
            file_name = s3_object.key.split('/')[-1]
            file_url = f'https://{self.BUCKET_NAME}.s3.amazonaws.com\
/{s3_object.key}'
            result[file_name] = file_url
        return result
