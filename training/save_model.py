import boto3

s3 = boto3.client("s3")
s3.upload_file("model.pkl", "mlops-fraud-models", "model.pkl")
print("Model uploaded to S3")
