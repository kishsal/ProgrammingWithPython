# Python CICD for Containers And Kubernetes

1. Git clone https://github.com/kizzle911/containerized-python
2. Update code as required
3. Go to Azure
    - Create new RG
    - Create Kubernetes resource
    - Choose latest version
    - Keep rest of the setting as default

4. Once Kubernetes is deployed, then go to deployment center
    - Click on Github
    - Choose Repo and branch
    - Create new namespace
    - Create new ACR
    - Deploy

5. This will create an Action in Github for this repo
    - Make sure to create an AZURE_CREDENTIALS and AKS_PYTHONBOOTCAMP_KUBECONFIG