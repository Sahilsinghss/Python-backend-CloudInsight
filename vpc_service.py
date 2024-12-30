import boto3

def get_vpc_and_subnets():
    session = boto3.Session(profile_name='serviceprofile')
    ec2_client = session.client('ec2')
    vpcs_info = []

    vpcs = ec2_client.describe_vpcs()['Vpcs']
    for vpc in vpcs:
        subnets_info = []
        subnets = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc['VpcId']]}])['Subnets']

        for subnet in subnets:
            subnets_info.append({
                "SubnetId": subnet['SubnetId'],
                "AvailabilityZone": subnet['AvailabilityZone'],
                "CIDRBlock": subnet['CidrBlock']
            })

        vpc_data = {
            "VPCId": vpc['VpcId'],
            "CIDRBlock": vpc['CidrBlock'],
            "State": vpc['State'],
            "Subnets": subnets_info
        }
        vpcs_info.append(vpc_data)

    return vpcs_info
