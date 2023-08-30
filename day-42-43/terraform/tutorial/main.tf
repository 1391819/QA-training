# specify required providers
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
}

# configure AWS provider
provider "aws" {
  region                  = "eu-west-2"
  shared_credentials_file = "~/.aws/credentials"
}

# create a new resource
resource "aws_instance" "EC2" {
  # declaring what Amazon Machine Image to use for the OS
  ami = var.ami-id
  # this will determine how many virtual CPUs and how much memory it will have
  instance_type = var.instance-type
  # key_name = var.pem-key # this is for ssh? would require a public key defined in the provider
}
