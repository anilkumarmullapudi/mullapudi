az aks scale --resource-group aks-practice-rg-india --name aks-practice-cluster --node-count 0


az aks nodepool add --resource-group aks-practice-rg-india --cluster-name aks-practice-cluster -name userpool1 --node-vm-size Standard_D2s_v3 --enable-cluster-autoscaler --min-count 0

az aks nodepool add --resource-group aks-practice-rg-india --cluster-name aks-practice-cluster --name userpool1 --node-vm-size Standard_D2s_v3 --enable-cluster-autoscaler --min-count 0 --max-count 2 --node-count 1

az aks nodepool scale --resource-group aks-practice-rg-india --cluster-name aks-practice-cluster --name userpool1 --node-count 0


**************************************************************************************************

 az --version
 az login --tenant TENANT_ID
 az login --tenant 8da0185f-5509-4d27-94fa-b4c855238d54
 az aks list --output table
 
 
 az provider show --namespace Microsoft.ContainerService --query "registrationState"
 az provider register --namespace Microsoft.ContainerService
 az provider show -n Microsoft.ContainerService

 az vm list-sizes --location eastus --output table
 az group create --name aks-practice-rg-india --location centralindia
 az aks create --resource-group aks-practice-rg-india --name aks-practice-cluster --node-vm-size     Standard_D2s_v3 --node-count 2
 
 az aks install-cli
TO Install kubectl  with az in your cli
az aks get-credentials --resource-group aks-practice-rg-india --name aks-practice-cluster



*********************************************************************************************

Step-by-Step: Push Image to ACR
Log in to Azure

powershell
az login
Create a Resource Group (if not already)

powershell
az group create --name myResourceGroup --location centralindia
Create an Azure Container Registry

powershell
az acr create --resource-group myResourceGroup --name myRegistryName --sku Basic
Replace myRegistryName with a unique name (ACR names must be globally unique).

--sku Basic is cost-effective for practice.

Log in to ACR

powershell
az acr login --name myRegistryName
Tag Your Local Docker Image for ACR
Suppose you built an image locally:

powershell
docker build -t myapp:v1 .
Tag it with your ACR login server:

powershell
docker tag myapp:v1 myregistryname.azurecr.io/myapp:v1
Push the Image to ACR

powershell
docker push myregistryname.azurecr.io/myapp:v1
Verify the Image in ACR

powershell
az acr repository list --name myRegistryName --output table
az acr repository show-tags --name myRegistryName --repository myapp --output t

*******************************************************************

az aks update -n aks-practice-cluster -g myResourceGroup --attach-acr anilpvtregistry


*****************************************************************8
Clean up cmsd's

az aks delete `
  --resource-group aks-practice-rg-india `
  --name aks-practice-cluster `
  --yes `
  --no-wait


az group delete --name aks-practice-rg-india --yes --no-wait

az network vnet list --resource-group aks-practice-rg-india --output table
az network public-ip list --resource-group aks-practice-rg-india --output table
az network lb list --resource-group aks-practice-rg-india --output table

az network vnet delete --resource-group aks-practice-rg-india --name <vnet-name>

Remove Managed Identities
AKS may create Managed Identities for cluster operations. Check:

powershell
az identity list --resource-group aks-practice-rg-india --output table

Delete the Resource Group (Optional)
If the resource group was dedicated to AKS and you don’t need anything else inside:

powershell
az group delete --name aks-practice-rg-india --yes --no-wait