#!/bin/python3
import boto3

ec2 = boto3.resource('ec2')

def deploy_instances():
    sum_instances = int(input("Enter how many instances:"))
    ami_type = input("Choose an OS for your instance:")
    instances = ec2.create_instances(
        ImageId=ami_type,
        MinCount=1,
        MaxCount=sum_instances,
        InstanceType='t2.micro',
        KeyName='projectkey'
    )

def terminate_instance():
    instances = input("Enter the IDs of the instances that you want to terminate (comma-separated):")
    ids = instances.split(',')
    ec2.instances.filter(InstanceIds=ids).terminate()

def describe_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()
    print(response)



def start_ec2_instance():
    instance_id = input("Enter the ID of the instance:")
    try:
        ec2.instances.filter(InstanceIds=[instance_id]).start()
        print(f"Successfully started EC2 instance with ID: {instance_id}")
    except Exception as e:
        print(f"Error starting EC2 instance: {str(e)}")

def stop_ec2_instance():
    instance_id = input("Enter the ID of the instance:")
    try:
        ec2.instances.filter(InstanceIds=[instance_id]).stop()
        print(f"Successfully stopped EC2 instance with ID: {instance_id}")
    except Exception as e:
        print(f"Error stopping EC2 instance: {str(e)}")

def main_menu():
    while True:
        print("Menu:")
        print("1. deploy-instances")
        print("2. start-instance")
        print("3. stop-instance")
        print("4. terminate-instances")
        print("5. describe-instances,6. Quit")



        choice = input("Enter your choice: ")

        if choice == "1":
            deploy_instances()
        elif choice == "2":
            start_ec2_instance()
        elif choice == "3":
            stop_ec2_instance()
        elif choice == "4":  # Fixed the typo here
            terminate_instance()
        elif choice == "5":
            describe_instance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Welcome to the EC2 management script!")
    main_menu()
