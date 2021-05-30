# Project2-Create S3 Bucket In AWS With AWS CDK

1. Create folder called "s3-bucket-aws-cdk"
2. CD into "s3-bucket-aws-cdk"
3. Then enter the following:
```
cdk init app --language python
```

4.  Go to `ProgrammingWithPython/Week5-IaCWithPython/Project2-CreateS3BucketInAWSWithPulumi/s3-bucket-aws-cdk/s3_bucket_aws_cdk/s3_bucket_aws_cdk_stack.py`
5. Enter code into file in "insert code section":
```
bucket = aws_s3.Bucket(self, "cloudskill_s3_bucket")
        print(bucket)
```
6. Ensure to import aws_s3
7. Save file

8. From the "s3-bucket-aws-cdk" directory, enter:
```
cdk deploy
```
