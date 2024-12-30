import json
from ec2_service import get_ec2_instances
from s3_service import get_s3_buckets
from vpc_service import get_vpc_and_subnets

def main():
    data = {
        "EC2Instances": get_ec2_instances(),
        "S3Buckets": get_s3_buckets(),
        "VPCs": get_vpc_and_subnets()
    }

    # Save the consolidated data to a JSON file
    with open('aws_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # Print the data to console
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
