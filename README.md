# AWS Credentials Handling for boto3 in Python

This project demonstrates how to handle AWS credentials securely in a Python application using `boto3`. We showcase two methods: using environment variables set on your local machine or CI/CD environment, and using a `.env` file for local development.

## Method 1: Environment Variables

For production environments or within CI/CD pipelines like GitHub Actions, we use environment variables. This is a secure method suitable for production-grade applications.

### Setting up in GitHub Actions

In your GitHub repository, go to `Settings` -> `Secrets` and add your AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`) as new secrets.

Your GitHub Actions workflow should be set up to inject these secrets as environment variables into the workflow run. Here's an example snippet from a workflow file:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: pip install boto3 pytest

      - name: Run tests
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: 'us-east-1' # Example region
        run: pytest

Method 2: .env File
For local development, we use a .env file at the root of our project. This file should contain your AWS credentials in the following format:

makefile
Copy code
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=your_region
Install the python-dotenv package to load these environment variables:

sh
Copy code
pip install python-dotenv
In your Python script, load the .env file and access your AWS credentials as follows:

python
Copy code
from dotenv import load_dotenv
load_dotenv()  # This will load the .env file

import os

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')

# Now you can use these credentials to configure your boto3 client
Make sure to add .env to your .gitignore file to prevent exposing your credentials.

Best Practices
Never commit your .env file or any sensitive keys to version control.
Always use encrypted secrets for storing sensitive information in CI/CD environments.
Keep your local .env file secure and do not share it.
Conclusion
This project provides a template for handling AWS credentials securely in a Python application for both local development and CI/CD pipelines.

typescript
Copy code

Make sure you replace placeholders like `your_access_key_id`, `your_secret_access_key`, and `your_region` with your actual AWS credentials in your `.env` file, and never share or commit this sensitive information to your repository.