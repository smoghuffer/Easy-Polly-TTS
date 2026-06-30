import os
import boto3
im

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
AWS_REGION = "eu-north-1"

if not ACCESS_KEY or not AWS_SECRET:
    raise ValueError(
        "missing AWS credentials, make sure to add them to your environment variables!"
    )

client = boto3.client(
    'polly',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name=AWS_REGION
)
