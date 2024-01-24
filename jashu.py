import boto3
lambda_Client = boto3.client('lambda', region_name='us-east-1')
response =lambda_Client.create_function(
            Code={
                'S3Bucket': 'jashu-test',
                'S3Key': 'test.py.zip', #how can i create or fetch this S3Key
            },

            FunctionName='testlambda3',
            Handler='test.py.lambda_handler',
            Publish=True,
            Role='arn:aws:iam::880305499190:role/lambda-ec2',
            Runtime='python3.12',
        )
