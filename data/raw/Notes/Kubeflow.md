## Installing kubectl for linux
```
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl

chmod +x ./kubectl

mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin

kubectl version --short --client
```
## Installing eksctl for cluster creation 
```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
```
## Creating cluster
```
eksctl create cluster --version=1.20 --name=amol-eks-cluster --node-private-networking --nodes=1 --spot --instance-types=t3.small --alb-ingress-access --region=us-east-2 --asg-access
```
## Scaling the cluster 
```
export NODEGROUP_NAME=$(eksctl get nodegroups --cluster amol-eks-cluster -o json | jq -r '.[0].Name')

eksctl scale nodegroup --cluster=amol-eks-cluster --nodes=6 --name=$NODEGROUP_NAME --nodes-min=0 --nodes-max=6
```
## Env Varialbles
```
cat << EoF > kf-install.sh
export AWS_CLUSTER_NAME=amol-eks-cluster
export KF_NAME=\${AWS_CLUSTER_NAME}

export BASE_DIR=${HOME}/environment
export KF_DIR=\${BASE_DIR}/\${KF_NAME}

# export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws_cognito.v1.0.1.yaml"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.1.yaml"

export CONFIG_FILE=\${KF_DIR}/kfctl_aws.yaml
EoF

source kf-install.sh
```
## Make working directory 
```
mkdir -p ${KF_DIR}
cd ${KF_DIR}
```
## Download Confirugation file
```
wget -O kfctl_aws.yaml $CONFIG_URI
```
## Edit Configuration file
```
sed -i '/region: us-east-2/ a \      enablePodIamPolicy: true' ${CONFIG_FILE}

sed -i -e 's/kubeflow-aws/'"$AWS_CLUSTER_NAME"'/' ${CONFIG_FILE}
sed -i "s@us-east-2@$AWS_REGION@" ${CONFIG_FILE}

sed -i "s@roles:@#roles:@" ${CONFIG_FILE}
sed -i "s@- eksctl-amol-eks-cluster-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@#- eksctl-amol-eks-cluster-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@" ${CONFIG_FILE}
```
## Issue Patching 
```
curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.15.10/2020-02-22/bin/linux/amd64/aws-iam-authenticator
chmod +x aws-iam-authenticator
sudo mv aws-iam-authenticator /usr/local/bin
```
## Deploy Kubeflow
```
cd ${KF_DIR}
kfctl apply -V -f ${CONFIG_FILE}
```
## Get Status 
```
kubectl -n kubeflow get all
```
## Open Dashboard
```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```
In your Cloud9 environment, click Tools / Preview / Preview Running Application 

## Deleting cluster 
```
eksctl delete cluster amol-eks-cluster
```
