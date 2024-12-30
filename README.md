Terraform Project: EC2, S3, and IAM Role
This Terraform project automates the creation of AWS resources, including EC2 instances, S3 buckets, and IAM roles. The EC2 instances are configured with full access to the S3 buckets through IAM policies.

Overview
This project includes:

EC2 instances created based on a specified AMI filter and type.
S3 buckets with names passed as input.
IAM roles and policies granting the EC2 instances full access to the S3 buckets.
The project is organized into modules for EC2 instances, S3 buckets, and IAM roles, which can be reused and customized.

Folder Structure
bash
Copy code
terraform-ec2/
│
├── main.tf               # Root module
├── variables.tf          # Input variables
├── outputs.tf            # Output variables
└── modules/
    └── ec2/
        ├── main.tf       # EC2 instance, AMI, and IAM logic
        ├── variables.tf  # Module input variables
        ├── outputs.tf    # Module output variables
    └── s3/
        ├── main.tf       # S3 bucket logic
        ├── variables.tf  # Module input variables
        ├── outputs.tf    # Module output variables
Prerequisites
Terraform v1.0 or later
AWS account and credentials configured (use aws configure or set environment variables)
Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-repository/terraform-ec2-s3-iam.git
cd terraform-ec2-s3-iam
2. Configure AWS Credentials
Make sure your AWS credentials are set up correctly. You can do this by either configuring the AWS CLI or exporting the AWS access key and secret key:

bash
Copy code
aws configure
Alternatively, you can export the credentials directly:

bash
Copy code
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
3. Initialize Terraform
Navigate to the root directory of the project and run the following command to initialize Terraform:

bash
Copy code
terraform init
4. Customize Variables (Optional)
Edit the main.tf file or create a terraform.tfvars file to customize variables such as:

instance_name: The name of the EC2 instance.
instance_type: The EC2 instance type (e.g., t2.micro).
ami_filter: The AMI filter string (e.g., amzn2-ami-hvm-*-x86_64-gp2).
ami_owner: The owner ID of the AMI (e.g., 137112412989).
You can also specify S3 bucket names by modifying the bucket_names variable in the S3 module.

5. Apply the Terraform Configuration
Once you’ve customized the configuration, apply the changes to create the resources:

bash
Copy code
terraform apply
Terraform will prompt you to confirm the plan. Type yes to proceed.

6. Verify the Resources
Once the resources are created, Terraform will output the following information:

EC2 instance ID: The ID of the created EC2 instance.
AMI ID: The ID of the selected AMI.
S3 ARNs: The ARNs of the created S3 buckets.
7. Destroy the Resources (Optional)
If you want to clean up the resources after use, run the following command:

bash
Copy code
terraform destroy
Terraform will prompt you to confirm the destruction. Type yes to proceed.

Module Details
EC2 Module
Creates an EC2 instance using a specified AMI.
IAM role: Automatically creates an IAM role and attaches a policy allowing full access to the S3 buckets.
Instance Profile: Attaches the IAM role to the EC2 instance via an instance profile.
S3 Module
Creates S3 buckets with the provided names.
Outputs the ARNs of the created buckets to be used by other modules.
IAM Role Module
Creates an IAM role for the EC2 instance.
Attaches a policy to the IAM role, granting full access to the S3 buckets created by the project.
Outputs
After applying the configuration, Terraform will output the following:

instance_id: The ID of the EC2 instance.
ami_id: The ID of the selected AMI.
s3_arns: The ARNs of the created S3 buckets.
Example Usage
You can call this Terraform module in another Terraform project:

hcl
Copy code
module "ec2_s3_iam" {
  source = "github.com/your-repository/terraform-ec2-s3-iam"

  instance_name = "ExampleInstance"
  instance_type = "t2.micro"
  ami_filter    = "amzn2-ami-hvm-*-x86_64-gp2"
  ami_owner     = "137112412989"
  bucket_names  = ["my-first-bucket", "my-second-bucket"]
}
Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

