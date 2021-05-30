# Project4-CreateIAMUseInAWSWithAWSCDK

1. Create folder called "iam-user-aws-cdk"
2. CD into "iam-user-aws-cdk"
3. Then enter the following:
```
cdk init app --language python
```

4.  Go to `ProgrammingWithPython/Week5-IaCWithPython/Project4-CreateIAMUseInAWSWithAWSCDK/iam-user-aws-cdk/iam_user_aws_cdk/iam_user_aws_cdk_stack.py`
5. Enter code into file in "insert code section":
```
iam_role=aws_iam.Role(
            self,
            id='lambdacsFullAccess',
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambda_FullAccess")
            ]
        )

        print(iam_role)

```
6. Ensure to `from aws_cdk import aws_iam`
7. Save file

8. From the "s3-bucket-aws-cdk" directory, enter:
```
cdk deploy
```

9. It will create a new role called  `IamUserAwsCdkStack-lambdacsFullAccess7072CE79-T55IZ454XMGD`