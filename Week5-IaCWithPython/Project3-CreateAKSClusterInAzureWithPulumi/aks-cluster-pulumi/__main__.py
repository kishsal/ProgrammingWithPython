"""An Azure RM Python Pulumi program"""

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

