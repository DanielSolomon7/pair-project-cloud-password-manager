import boto3
from pprint import pprint
import os

def warm_up_s3():
    s3 = boto3.client('s3')

    bucket_name = "warm-up-bucket-nc-06-11-2024"

    ''' Create s3 bucket '''
    s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                         'LocationConstraint': 'eu-west-2'
                     })

    ''' Make file1 '''
    with open('file1.txt', 'w', encoding='utf-8') as file:
        file.write("Text of file1!")
        file1_name = 'file1.txt'
    s3.upload_file(file1_name, bucket_name, file1_name)

    ''' Make file2 '''
    with open('file2.txt', 'w', encoding='utf-8') as file:
        file.write("Text of file2!")
        file2_name = 'file2.txt'
    s3.upload_file(file2_name, bucket_name, file2_name)

    ''' List file names '''
    response = s3.list_objects_v2(Bucket=bucket_name).get("Contents")
    bucket_files = [file['Key'] for file in response]
    print(f"Files in s3 bucket: {bucket_files}", end="\n\n")

    ''' Prints content of file1 to terminal '''
    file_1 = response[0]["Key"]
    file_2 = response[1]["Key"]
    new_response = s3.get_object(Bucket=bucket_name, Key=file_1)
    object_content = new_response["Body"].read().decode("utf-8")
    print(f"Contents of {file_1}\n-----------------------------")
    print(object_content, end="\n\n")

    ''' Delete files in s3 bucket '''
    s3.delete_objects(
        Delete={
            'Objects': [
                {'Key': file_1},
                {'Key': file_2}
            ]
        },
        Bucket=bucket_name
    )

    ''' Delete s3 bucket '''
    s3.delete_bucket(
        Bucket=bucket_name
    )

    ''' Show that there are no buckets '''
    pprint(f'Current buckets: {s3.list_buckets()['Buckets']}')


    ''' Delete files '''
    os.remove('file1.txt')
    os.remove('file2.txt')





warm_up_s3()
