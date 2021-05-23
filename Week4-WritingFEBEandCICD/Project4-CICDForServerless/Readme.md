# Python CICD for Serverless

## In Azure

1. Go to Web App Service
2. Create new Web App
    - Provide RG
    - Provide a webapp name
    - Choose python 3.8
    - Choose F1 SKU
    - Create

3. Once the webapp is deployed..
    - Click on the resource
    - Click on Deployment center
    - Choose Github as source
    - Choose Org, Repo and Branch
    - Choose Python and version 3.8
    - Save

4. Now if you go to GitHub --> Actions, you will see a build and deploy.

