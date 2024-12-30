import boto3

def get_ec2_instances():
    # Use a specific profile (if configured in ~/.aws/credentials)
    session = boto3.Session(profile_name='serviceprofile')
    ec2_client = session.client('ec2')
    instances_info = []

    instances = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )['Reservations']

    for reservation in instances:
        for instance in reservation['Instances']:
            instance_data = {
                "InstanceId": instance.get('InstanceId'),
                "State": instance['State']['Name'],
                "InstanceType": instance.get('InstanceType'),
                "PublicIP": instance.get('PublicIpAddress'),
                "PrivateIP": instance.get('PrivateIpAddress'),
                "KeyName": instance.get('KeyName'),
                "LaunchTime": instance.get('LaunchTime').strftime("%Y-%m-%d %H:%M:%S"),
                "Tags": {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            }
            instances_info.append(instance_data)

    return instances_info
