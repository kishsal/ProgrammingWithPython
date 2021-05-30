# Project1-CreateAStorageAccountInAzureWithPulumi

1. Go to pulumi.com
2. Authenticate with github account
3. Click on Project and create new project
4. Choose Azure and Python
5. Provide a project name, set stack to dev and location to EastUs
6. Go to Project directory
7. Enter the following:
```
mkdir azure-python-cloudskill-python && cd azure-python-cloudskill-python
```

8. Pull down project to get started, by entering:
```
pulumi new azure-python -s kizzle911/azure-python-cloudskill-python/dev
```

9. Deploy it, by entering:
```
pulumi up
```

Received error: 
```
ksalgado-mn2:azure-python-cloudskill-python ksalgado$ pulumi up
Previewing update (dev)

View Live: https://app.pulumi.com/kizzle911/azure-python-cloudskill-python/dev/previews/74376398-5db7-47b6-adbe-d132f4c961f0

     Type                                     Name                                Plan     Info
     pulumi:pulumi:Stack                      azure-python-cloudskill-python-dev           
     └─ azure-native:resources:ResourceGroup  resource_group                               1 error
 
Diagnostics:
  azure-native:resources:ResourceGroup (resource_group):
    error: building authorizer: Error obtaining Authorization Token from the Azure CLI: Error parsing json result from the Azure CLI: Error waiting for the Azure CLI: exit status 1
```