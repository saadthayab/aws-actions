import boto3
import os
import pytest
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv('.env')  # Specify the path to your .env file


@pytest.fixture(scope="module")
def iam_client():
    """Create an IAM client using Boto3"""
    # Environment variables are now loaded from the .env file
    return boto3.client(
        'iam',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )


def test_iam_user_exists(iam_client):
    """Test if an IAM user named 'eks-saad' exists"""
    user_name = "eks-saad"
    try:
        response = iam_client.get_user(UserName=user_name)
        assert response and response.get('User'), f"User '{user_name}' does not exist."
    except iam_client.exceptions.NoSuchEntityException:
        pytest.fail(f"IAM User '{user_name}' does not exist.")
