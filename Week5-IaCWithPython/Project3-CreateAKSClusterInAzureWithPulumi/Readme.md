# Create AKS Cluster in Azure with Pulumi

1. Go to pulumi.com
2. Authenticate with github account
3. Click on Project and create new project
4. Choose Azure and Python
5. Provide a project name, set stack to dev and location to EastUs
6. Go to Project directory
7. Enter the following:
```
mkdir aks-cluster-pulumi && cd aks-cluster-pulumi
```

8. Pull down project to get started, by entering:
```
pulumi new azure-python -s kizzle911/aks-cluster-pulumi/dev
```

9. Update code in `__main__.py`
```
import pulumi
from pulumi_azure import containerservice, core

containerservice.KubernetesCluster(
    resource_name='csaks20210530'
    default_node_group={
        'min_count': 1,
        "max_count": 1,
        'name': 'csaks20210530',
        'vm_size': 'Standard_d2_v2',
        'enable_auto_scaling': True
    },
    dns_prefix='csdns',
    resource_group_name='cs-rg',
    service_principal={
        'client_id':'',  # clientId from Service Principal in Azure
        'client_secret':'' # client secret
    }
)

```

9. Deploy it, by entering:
```
pulumi up
```