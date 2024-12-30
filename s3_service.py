import boto3

def get_s3_buckets():
    session = boto3.Session(profile_name='serviceprofile')
    s3_client = session.client('s3')
    buckets_info = []

    response = s3_client.list_buckets()
    for bucket in response.get('Buckets', []):
        bucket_data = {
            "BucketName": bucket['Name'],
            "CreationDate": bucket['CreationDate'].strftime("%Y-%m-%d %H:%M:%S")
        }
        buckets_info.append(bucket_data)

    return buckets_info
