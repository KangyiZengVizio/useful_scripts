#!/usr/bin/env python3
# This is the script to quick loop through s3 bucket with specific prefix. 
# its useful when you are dealing with millions of files but file has specific prefix.
import boto3
import fnmatch
import logging
# Create a boto3 client for s3
s3 = boto3.Session(profile_name='AAA').client('s3')

# Specify the bucket name and prefix
bucket_name = 'A-log'
prefix = 'cloudfront-logging/aaa.2023-11-16-'
# Get a list of all objects in the bucket with the prefix
objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)['Contents']

for obj in objects:
    # Construct the new key by replacing the prefix with the new folder name
    new_key = obj['Key'].replace(prefix, '20231116-latest/aaa.2023-11-16-')

    # Copy the object to the new key
    s3.copy_object(Bucket=bucket_name, CopySource=f"{bucket_name}/{obj['Key']}", Key=new_key)
