import boto3
import os
import pytest


@pytest.fixture(scope="module")
def iam_client():
    """Create an IAM client using Boto3"""
    return boto3.client('iam',
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                        region_name=os.environ.get('AWS_DEFAULT_REGION'))


def test_iam_user_exists(iam_client):
    """Test if an IAM user named 'eks-saad' exists"""
    user_name = "eks-saad"
    try:
        response = iam_client.get_user(UserName=user_name)
        assert response and response.get('User'), f"User '{user_name}' does not exist."
    except iam_client.exceptions.NoSuchEntityException:
        pytest.fail(f"IAM User '{user_name}' does not exist.")
