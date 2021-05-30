#Lecture Demo

## Pulumi

1. Go to https://www.pulumi.com/ and either sign up or sign in if you already have a Pulumi account. Pulumi is free for individual use, so you can sign up without any charge. You have a few options to use to sign up. In my case, I signed up through my GitHub.
2. Once you're signed up, go to Projects and click the + Create project button.
3. Choose the cloud and programming language. In my case, I'll go with AWS and Python.
4. Give the project a name, description, choose a stack name, and specify the AWS region.
5. Click Create project
6. Follow the instructions on the getting Get started page for your operating system.
7. Install Pulumi CLI
```
brew install pulumi
```

8. Create a new directory for your project and change into it.
```
mkdir lecture-demo-cloudskills && cd lecture-demo-cloudskills
```
9.  Pull down your project to get started.
```
pulumi new aws-python -s kizzle911/lecture-demo-cloudskills/dev
```
10. Deploy it
```
pulumi up
```

11. You will notice a venv enviroment (python virtual environment)


## AWS
1. Download the AWS CDK for your operating system. Because I'm on a Mac, I'll use Brew. https://docs.aws.amazon.com/cdk/latest/guide/cli.html

2. Open up the terminal and inside of the directory where you want your new CDK app to exist, run the following command: cdk init app --language python

3. You'll now see several different files and directories.

4. Notice how there's a requirements.txt file, which are the Python requirements needed to install the AWS CDK. Run: pip3 install -r requirements.txt

5. Run cdk deploy and you'll see the new CloudFormation stack being created.

6. Run cdk destroy to destroy the CDK project in AWS